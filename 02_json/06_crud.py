import json


def fetch_items(file):
    with open(file=file, mode="r", encoding="utf-8") as json_file:
        return json.load(json_file)


employees = fetch_items("./files/new_employees.json")


def get_all_employees():
    return employees


def find_employee(id):
    for employee in employees:
        if employee["id"] == id:
            return employee
    return None


def update_employee(id, updated_employee):
    employee = find_employee(id)
    if employee is None:
        return None
    employee.update(updated_employee)
    return employee


def create_employee(employee):
    new_employee = employee.copy()
    new_employee.update({"id": employees[-1]["id"] + 1})
    employees.append(new_employee)
    return new_employee


def remove_employee(id):
    employee = find_employee(id)
    if employee is not None:
        employees.remove(employee)
    return employee


if __name__ == "__main__":
    # print(get_all_employees())
    # print(find_employee(10))
    # print(update_employee(1, {'first_name': 'Gergely', 'last_name': 'Gáll'}))
    # print(create_employee({'first_name': 'Johnny', 'last_name': 'Boy'}))
    remove_employee(1)
    print(find_employee(1))
