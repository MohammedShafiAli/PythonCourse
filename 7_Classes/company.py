from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        for i in self.employees:
            print(i.fname, i.lname)
        print("----------------")

    def pay_employees(self):
        for i in self.employees:
            print("Paycheck for:", i.fname, i.lname)
            print(f"Amount: £{i.calculate_paycheck():,.2f}")
            print("--------------------")


def main():
    my_company = Company()

    employee1 = Employee("Ali", "Khan", 50000)
    my_company.add_employee(employee1)
    employee2 = Employee("Joe", "Patel", 40000)
    my_company.add_employee(employee2)
    employee3 = Employee("Lee", "Frank", 45000)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()