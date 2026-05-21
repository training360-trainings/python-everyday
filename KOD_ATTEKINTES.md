# Kód-áttekintés — oktatási anyag

**Dátum:** 2026-05-21
**Hatókör:** `01_csv`, `02_json`, `03_xml`, `04_xlsx`, `05_db-mail-api`, `06_pandas`, `07_matplotlib`, `08-gml`, `project`
(A kísérleti/ideiglenes fájlok — `t.py`, `05_db-mail-api/n.py`, `06_pandas/t.py`, `06_pandas/t.ipynb` — nincsenek áttekintve; ezek láthatóan piszkozatok, **érdemes törölni** őket, hogy a tananyag tiszta maradjon.)

> A jelölt **valódi hibákat már kijavítottam** a kódban (lásd lentebb). A „javaslat” jelölésűeket szándékosan **nem** írtam át, mert oktatói döntést igényelnek vagy notebook-kimeneteket érintenének.

---

## 1. Összefoglaló

| Súlyosság | Db | Mi | Állapot |
|-----------|----|----|---------|
| 🔴 Kritikus | 4 | Nem fut le / hibás eredményt ad | ✅ Javítva |
| 🟠 Magas | 3 | Modern verzión törik (matplotlib stílus, pandas elavult API) | 💡 Javaslat |
| 🟡 Közepes | 3 | Hiányzó adatfájlok, félrevezető útvonalak, biztonsági minta | 💡 Javaslat |
| ⚪ Alacsony | több | Stílus, konzisztencia, elgépelés | 💡 Javaslat |

---

## 2. 🔴 Kritikus hibák — KIJAVÍTVA

### `01_csv/07-stat.py` — hibás átlagszámítás
- **39. sor:** ottfelejtett `print(type(values[0]))` debug sor.
- **40. sor:** `stat["count"] = sum(values)` — a darabszám az **összeg** lett, így a 44. sori átlag `sum / sum`, azaz **mindig ~1.0**.
- **Javítás:** `stat["count"] = len(values)`, debug sor törölve.
- **Ellenőrzés:** futtatás után reális eredmény: `avg ≈ 118082.8`, `count = 1000`. ✅

### `05_db-mail-api/01_db.py` — felcserélt `sum` és `avg`
- **39–40. sor:** a `"sum"` kulcs az **átlagot**, az `"avg"` kulcs az **összeget** adta vissza.
- **Javítás:** a két érték felcserélve a helyes kulcsokra.
- (Megjegyzés: a `01_csv/07-stat.py` és ez a fájl ugyanazt a statisztikát számolja — érdemes a két leckét összhangban tartani.)

### `02_json/06_crud.py` — induláskor összeomlott
- **1. sor:** `from jsonmodule import fetch_items` — **nem létező modul**, a fájl már importáláskor `ModuleNotFoundError`-ral elszállt.
- **4. sor:** a `fetch_items(...)` hívás a függvény definíciója *előtt* állt.
- **`update_employee` / `remove_employee`:** `find_employee` `None`-t is adhat, amin `.index(None)` / `.remove(None)` crashel.
- **Javítás:** a hamis import törölve; `fetch_items` `with`-tel olvas és a definíció után hívjuk; a CRUD-függvények None-ellenőrzést kaptak.
- **Megjegyzés:** futáshoz hiányzik a `02_json/files/new_employees.json` adatfájl (lásd 4. pont) — a kód logikailag már helyes.

### `02_json/07_crud_reusable.py` — hiányzó függvényparaméter
- **13. és 27. sor:** `find_item(id)` a `find_item(items, id)` helyett — `TypeError`-t dobott.
- **Javítás:** helyes hívás + None-ellenőrzés.
- **Ellenőrzés:** szintetikus adattal tesztelve (update/remove + hiányzó id eset) — nem crashel. ✅

---

## 3. 🟠 Magas — modern verzión törik (javaslat)

### Elavult matplotlib stílus
`07_matplotlib/03-save-charts.py`, `04-data-analysis.py`, `05-data-analysis-csv.py`:
```python
plt.style.use('seaborn-v0_8-bright')
```
A `seaborn-v0_8-*` stílusok matplotlib 3.6 óta elavultak, újabb verziókban figyelmeztetést/hibát adhatnak. **Javaslat:** `'ggplot'` vagy `'default'`, illetve a `seaborn` csomag `sns.set_theme()` használata.

### Pandas notebookok — elavult API-k
- `06_pandas/10-add-remove-cols.ipynb`: `df.append(...)` — **pandas 2.0-ban megszűnt**. Helyette `pd.concat([df, uj], ignore_index=True)`.
- `06_pandas/07-update-df.ipynb`: `df.applymap(...)` — pandas 2.1 óta elavult, helyette `df.map(...)`.
- Sok notebookban (`07,09,10,11,12,13`) bőséges `inplace=True`. Nem hibás, de a modern pandas a láncolható, érték-visszaadó stílust ajánlja.

> Ezeket szándékosan nem írtam át: notebook-cellák szerkesztése a tárolt kimeneteket is érinti, és oktatói döntés, mennyire akarod a régi API-t bemutatni (akár szándékosan, „így ne csináld” példaként).

---

## 4. 🟡 Közepes (javaslat)

### Hiányzó adatfájlok
A `02_json` mappában nincs `files/` könyvtár, így a `new_employees.json`, illetve több lecke adatfájlja hiányzik a repóból. A kód helyes, de **az adatok nélkül a leckék nem futtathatók**. Javaslat: az adatfájlokat verziózni (vagy egy `files/`-generáló szkriptet mellékelni).

### Félrevezető útvonalak a notebookokban
- `07-update-df.ipynb`, `09-sorting-advanced.ipynb`, `12-grouping-aggregating.ipynb`: `pd.read_csv('stackowerflow/survey_results_public.csv', ...)` — elgépelt/rossz mappanév (valószínűleg `files/` kellene). `FileNotFoundError`.
- `13-datateime.ipynb`: `ETH_1h.csv` nem létezik; a hibás cella miatt a notebook lánca megszakad (`df` undefined a következő cellában). Itt egy nem használt `date_formatter()` is zavart kelt.

> Ezeket nem írtam át vakon — előbb tisztázni kell a tényleges adatkönyvtárat.

### Biztonsági minta (oktatási, nem valós szivárgás)
- `05_db-mail-api/01_db.py`: beégetett (dummy) DB-jelszó.
- `05_db-mail-api/04-send_mail.py`, `project/mailer.py`: placeholder e-mail jelszó.

Nem valós titok, de **rossz szokást taníthat**. Javaslat: mutasd be az `os.getenv("DB_PASSWORD")` / `.env` mintát — ez maga is hasznos lecke.

---

## 5. ⚪ Alacsony — stílus, konzisztencia (javaslat)

### Erőforrás-kezelés (`with` hiánya)
A fájlt megnyitják, de nem `with`-tel zárják:
- `02_json/02_read_json.py`, `02_json/05_stat.py`, `01_csv/04_use_generator.py` (generátorban a fájl csak a bejárás végén záródik).

Működnek, de pont az ellenkezőjét tanítják annak, amit kellene. Javaslat: mindenhol `with open(...) as f:`.

### Konzisztencia a hasonló leckék közt
- **`encoding`:** néhol `encoding="utf-8"`, néhol semmi. Javaslat: mindenhol egységesen megadni.
- **Hibaüzenetek nyelve:** keverten magyar/angol (`01_csv/06-filter-cols.py`, `04_xlsx/06-filter-cols.py`, kommentek). Javaslat: válassz egy nyelvet.
- **JSON-formázás:** `02_json/03_write_json.py` nem ad `indent`-et, míg `04_append.py` igen (`indent=4, ensure_ascii=False`). Érdemes egységesíteni.
- **Paraméter-árnyékolás:** `01_csv/01_read.py`, `02_skip-header.py`, `03_columns-and-data.py` az `open(file=file, ...)`-ban újrahasználja a `file` paramétert — kezdőknek zavaró.

### Apróságok
- `01_csv/08_write_lists.py` és `04_xlsx/08_write_lists.py`: nem használt `from os import path`.
- `07_matplotlib/04-data-analysis.py`: a `dev_y` importálva, de nem használt (a többi import rendben).
- `07_matplotlib/05-data-analysis-csv.py`: `plt.ylabel("PRogramming languages")` elgépelés + `"./files//survey_light.csv"` dupla perjel.
- `03_xml/03_use_generators.py`: a generátort rögtön `list()`-tel materializálja — épp a generátor lényegét oltja ki.
- `03_xml/07_append.py`: modul-szintű példakód `if __name__ == "__main__":` blokk nélkül (importáláskor lefut).

### Elnevezések (átnevezés külön kérésre)
- `06_pandas/04_df_from_scources.ipynb` → `04_df_from_sources.ipynb`
- `06_pandas/13-datateime.ipynb` → `13-datetime.ipynb`
- `06_pandas/16-big_data_gen_multiproc.py`: a név „multiproc”, de **Dask**-ot használ (nem a `multiprocessing` modult). Maga a kód helyes (a `dd.to_numeric` létezik) — csak a fájlnév félrevezető.

---

## 6. Amit az automatikus elemzés tévesen jelzett (cáfolva)
A teljesség kedvéért — ezek **nem** hibák:
- `07_matplotlib/04-data-analysis.py`: a `dev_y` **létezik** a `snippets.py`-ban, és a `numpy` **használt** (`np.arange`). Nem import-hiba (csak `dev_y` felesleges).
- `06_pandas/16-big_data_gen_multiproc.py`: a `dd.to_numeric` **létező** Dask-függvény.

---

## 7. Mit változtattam meg ténylegesen
| Fájl | Változás |
|------|----------|
| `01_csv/07-stat.py` | `count = len(values)`; debug `print` törölve |
| `05_db-mail-api/01_db.py` | `sum`/`avg` kulcsok helyreállítva |
| `02_json/06_crud.py` | hamis import törölve; `with`-es olvasás; None-ellenőrzés a CRUD-ban |
| `02_json/07_crud_reusable.py` | `find_item(items, id)` helyes hívás; None-ellenőrzés |

Minden módosított fájl `py_compile`-lal és (ahol volt adat) futtatással ellenőrizve.
