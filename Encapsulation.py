#Encapsulation - Hide the data and allow access only through controlled methods.
"""
class Bankaccount:
    def __init__(self):
        self._balance = 5000

bank = Bankaccount()
print(bank._balance)


class BankAccount:
    def __init__(self):
        self.__balance = 5000
    def show_balance(self):
        print(self.__balance)
        
Bank = BankAccount()
Bank.show_balance()
"""

#Example - 1
"""
class Bank:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print(self.__balance)
        
amount = Bank()
amount.deposit(5000)
amount.show_balance()
"""
#Example - 2
"""
class Bank:
    def __init__(self):
        self.__balance = 10000
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:   
            print("Insufficient Balance")
    def show_balance(self):
        print(self.__balance)

        
amount = Bank()
amount.withdraw(999)
amount.show_balance()
"""

#Example - 3
"""
class Employee:
    def __init__(self):
        self.name = "Saksham"
        self._salary = 100000
        self.__password = 'abc123'
        
emp = Employee()
print(emp.name)
print(emp._salary)
print(emp.__password)
"""

#Practice - 1
"""
class BankAccount:
    def __init__(self):
        self.__balance = 1000
    def show_balance(self):
        print(self.__balance)
        
bank = BankAccount()
bank.show_balance()
"""
#Practice - 2
"""
class Student:
    def __init__(self):
        self.__marks = 90
    def show_marks(self):
        print(self.__marks)
        
stu1 = Student()
stu1.show_marks()
"""

#Practice - 3
"""
class Employee:
    def __init__(self):
        self.__salary = 50000
    def show_salary(self):
        print(self.__salary)
        
emp = Employee()
emp.show_salary()
"""

#Mini Challenge
"""
class ATM:
    def __init__(self):
        self.__balance = 10000
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
    def show_balance(self):
        print(self.__balance)
        
amount = ATM()
amount.deposit(5000)
amount.show_balance()
amount.withdraw(2000)
amount.show_balance()
"""
