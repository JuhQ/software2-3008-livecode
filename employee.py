from base_employee import Employee

class HourlyPaid(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.hourly_salary = salary

    class Car:
        def __init__(self):
            print("Car")

    def print(self):
        self.money = 5000
        super().print()
        super().take_money_from_bank_account()
        print(f"Hourly salary: {self.hourly_salary}")
        print(self.money)

class MonthlyPaid(Employee):
    def __init__(self, name, salary):
        self.name = f"Monthly {name}"
        self.monthly_salary = salary
        super().__init__(name)
