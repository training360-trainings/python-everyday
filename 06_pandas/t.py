from matplotlib import pyplot as plt
import numpy as np

# Mintaadatok generálása
data1 = np.random.normal(0, 1, 1000)  # Normál eloszlás (átlag=0, szórás=1)
data2 = np.random.normal(3, 2, 1000)  # Normál eloszlás (átlag=3, szórás=2)

# Ábra létrehozása 1 sorral és 2 oszloppal
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Első hisztogram (bal oldali)
ax1.hist(data1, bins=25, color="blue", alpha=0.7, edgecolor="black")
ax1.set_title("Első adatsor")
ax1.set_xlabel("Érték")
ax1.set_ylabel("Gyakoriság")
ax1.grid(True, alpha=0.3)

# Második hisztogram (jobb oldali)
ax2.hist(data2, bins=25, color="green", alpha=0.7, edgecolor="black")
ax2.set_title("Második adatsor")
ax2.set_xlabel("Érték")
ax2.set_ylabel("Gyakoriság")
ax2.grid(True, alpha=0.3)

# Egész ábra címe
fig.suptitle("Két hisztogram összehasonlítása", fontsize=16)
plt.tight_layout()
plt.savefig("ket_hisztogram.png")
plt.show()
