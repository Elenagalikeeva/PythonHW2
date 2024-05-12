from Salary import salaryempoyee, hourlyemployee, commissionempoyee, payrollsystem


# def run():
salary_employee = salaryempoyee.SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = hourlyemployee.HourlyEmployee(2, "Илья Кромин", 40, 15)
commission_employee = commissionempoyee.CommissionEmployee(3, "Николай Хорольский", 1000, 250)
payroll_system = payrollsystem.PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commission_employee
])


# if __name__ == '__hw29__':
#     run()
