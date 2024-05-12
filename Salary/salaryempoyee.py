class Employee:
    def __init__(self, kod, name):
        self.id = kod
        self.name = name


class SalaryEmployee(Employee):
    """Административные работники, имеют фиксированную зарплату"""

    def __init__(self, kod, name, weekly_salary):
        super().__init__(kod, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
