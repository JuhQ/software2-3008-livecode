class Employee:
    number = 0
    def __init__(self, name):
        self.name = name
        Employee.number = Employee.number + 1
        self.employee_number = Employee.number

    def print(self):
        print(f"{self.name} - {self.employee_number}")

    def take_money_from_bank_account(self):
        self.money = 0
