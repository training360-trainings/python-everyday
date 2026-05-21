import csv


def validate_columns(file_columns, required_columns):
    missing_columns = [col for col in required_columns if col not in file_columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    return [file_columns.index(col) for col in required_columns]


def read_csv_file_generator(file_path, required_columns):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        columns = next(reader)

        col_indices = validate_columns(columns, required_columns)

        yield required_columns

        for row in reader:
            filtered_row = [row[i] for i in col_indices]
            yield dict(zip(required_columns, filtered_row))


def calculate_statistics(file_path, column_name):
    gen = read_csv_file_generator(file_path, [column_name])
    values = []
    stat = {"min": None, "max": None, "sum": None, "avg": None, "count": 0}

    for row in gen:
        try:
            value = float(row[column_name])
            values.append(value)
        except (ValueError, TypeError):
            continue

    if len(values) > 0:
        print(type(values[0]))
        stat["count"] = sum(values)
        stat["min"] = min(values)
        stat["max"] = max(values)
        stat["sum"] = sum(values)
        stat["avg"] = stat["sum"] / stat["count"]

    return stat


if __name__ == "__main__":
    stat = calculate_statistics("./files/employees-with-header.csv", "yearly_salary")
    print(stat)
