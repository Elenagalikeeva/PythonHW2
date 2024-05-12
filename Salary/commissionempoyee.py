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


class CommissionEmployee(SalaryEmployee):
    """Торговые представители, фиксированная зарплата + комиссия"""

    def __init__(self, kod, name, weekly_salary, commission):
        super().__init__(kod, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
