"""
Assignment name: Override Class Methods Assignment
Program: Employee.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use derived classes in multiple other classes (salaried and hourly derive
variables from the employee class) and then using (overridden) functions to display information about the
employee and to use function to give raises in each derived class.
"""


# Employee class (base class)
class Employee:
    def __init__(self, last_name, first_name, address, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def display(self):
        return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.phone_number)}\n{str(self.address)}'
