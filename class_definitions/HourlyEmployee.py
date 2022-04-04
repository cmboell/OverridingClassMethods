"""
Assignment name: Override Class Methods Assignment
Program: HourlyEmployee.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use derived classes in multiple other classes (salaried and hourly derive
variables from the employee class) and then using (overridden) functions to display information about the
employee and to use function to give raises in each derived class.
"""
# import
from datetime import datetime
from class_definitions.Employee import Employee


# hourly employee class (derived)
class HourlyEmployee(Employee):
    def __init__(self, lname, fname, phone, addy, start_date, hourly_rate):
        super().__init__(lname, fname, phone, addy)
        dateformat = datetime.strptime(start_date, '%m-%d-%Y')
        self.start_date = dateformat.strftime('%m-%d-%Y')
        self.hourly_rate = hourly_rate

    # give raise function
    def give_raise(self, hourly_rate):
        self.hourly_rate = hourly_rate

    # display function
    def display(self):
        return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.phone_number)}\n{str(self.address)}\nHourly Employee: $' + '%.2f' % float(self.hourly_rate) + '/hour\nStart Date: ' + self.start_date


# Driver
if __name__ == "__main__":
    he = HourlyEmployee('Boell', 'Colby', '888-999-1111', '123 N. Main St\nTownsville, IA 51401', '04-03-2022', 10.00)
    print(he.display())
    he.give_raise(12.00)
    print(he.display())
