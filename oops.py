#Object & Classes
#Class
"""

class Student:
    name = "Saksham"
    
#Object
S1 = Student
print(S1.name)

"""

"""
class Car:
    color = "Black"
    car_name = "Hilux"
    
Toyota = Car()
print(Toyota.color)
print(Toyota.car_name)

"""

#Constructor
#__init__ function - All function have a function called __init__ function which is always exceuted when the object is initiated
"""
class student:
    name = "Saksham"
    def __init__(self):
        print(self)
        print("Adding myself in database")
S1 = student()
print(S1)
"""
#self is a default constructor and with self like name, marks are parameterized constructor
"""
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding myself in database")
S1 = student("Saksham", 100)
print(S1.name,S1.marks)

S2 = student("Boogy",99)
print(S2.name,S2.marks)
"""

class Account:  # Class names should start with a capital letter
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total Balance:", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance:", self.get_balance())

    # Check balance
    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(1000)
        
    