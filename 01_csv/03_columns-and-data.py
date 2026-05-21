import csv


def read_csv_file(file):
    with open(file, "r") as file:
        reader = csv.reader(file)
        content = [row for row in reader]
        return content[0], content[1:]


if __name__ == "__main__":
    columns, data = read_csv_file("./files/employees-with-header.csv")
    print("Columns: ", columns)
    print("Data: ", data)
    