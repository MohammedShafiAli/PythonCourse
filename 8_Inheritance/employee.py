class Employee(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hours_worked, hourly_rate):
        super().__init__(fname, lname)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.hours_worked*self.hourly_rate
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.comission_rate = commission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_comission = self.sales_num*self.comission_rate
        return regular_salary + total_comission