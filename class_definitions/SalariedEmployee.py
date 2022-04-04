"""
Assignment name: Override Class Methods Assignment
Program: SalariedEmployee.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use derived classes in multiple other classes (salaried and hourly derive
variables from the employee class) and then using (overridden) functions to display information about the
employee and to use function to give raises in each derived class.
"""
# import
from datetime import datetime
from class_definitions.Employee import Employee


# salaried employee class
class SalariedEmployee(Employee):
    def __init__(self, lname, fname, phone, addy, start_date, salary):
        super().__init__(lname, fname, phone, addy)
        dateformat = datetime.strptime(start_date, '%m-%d-%Y')
        self.start_date = dateformat.strftime('%m-%d-%Y')
        self.salary = salary

    # give raise function
    def give_raise(self, salary):
        self.salary = salary

    # display function
    def display(self):
        return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.phone_number)}\n{str(self.address)}\nSalaried Employee: $' + '%.2f' % float(self.salary) + '/year\nStart Date: ' + self.start_date


# Driver
if __name__ == "__main__":
    se = SalariedEmployee('Boell', 'Colby', '111-222-3333', '131 E. New St\nPlain, IA 51401', '04-03-2022', 40000.00)
    print(se.display())
    se.give_raise(45000.00)
    print(se.display())
