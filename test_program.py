from employee import HourlyPaid, MonthlyPaid

employee1 = HourlyPaid("Juha", 10)
employee1.print()
print(employee1.employee_number)

employee2 = MonthlyPaid("Juha", 100)
employee2.print()

car = HourlyPaid.Car()
