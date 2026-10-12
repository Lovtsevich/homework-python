"""Это docstring модуля tests.py."""
from company import employees
from utils import get_employee_by_id
from utils import get_active_employees

# Проверка поиска по employee_id
assert get_employee_by_id(employees, 3)["name"] == "Сергей Ковалев"
assert get_employee_by_id(employees, 999) is None
print("Все тесты успешно пройдены")

# Список работающих сотрудников
active = get_active_employees(employees)
assert len(active) > 0
assert all(employee["fire_year"] is None for employee in active)
print("Все тесты успешно пройдены")
