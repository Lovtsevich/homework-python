"""Это docstring модуля utils.py."""
# Поиск сотрудников. Вернуть сотрудника по ID.
def get_employee_by_id(employees, employee_id):
    """Это docstring функции get_employee_by_id"""
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None


# Список работающих сотрудников
def get_active_employees(employees):
    """Это docstring функции get_active_employees"""
    list_active_employees = []
    for employee in employees:
        if employee["fire_year"] is None:
            list_active_employees.append(employee)
    return list_active_employees
