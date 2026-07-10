"""
class Animal:
    def sound(self):
        print("some sound")
class Dog(Animal):
    def sound(self):
        print("Whoof Whoof")
dog1 = Dog()
dog1.sound()


class Vehicle:
    def start(self):
        print("Vehicle Started")
class Bike:
    def start(self):
        print("Bike Started")
bike1 = Bike()
bike1.start()

class Employee:
    def work(self):
        print("Employees working")
class developer(Employee):
    def work(self):
        print("Writing Code")
dev1 = developer()
dev1.work()

"""

#Practice1 
"""
class Animal:
    def Move(self):
        print("Animal Moving")
class Bird:
    def Move(self):
        print("Bird Moving")
        
bird1 = Bird()
bird1.Move()


class Payment:
    def pay(self):
        print("Payment Processing")
class Creditcard:
    def pay(self):
        print("Credit Card Payment Processing")
Creditcard1 = Creditcard()
Creditcard1.pay()



class Notification:
    def send(self):
        print("Sending Notification")
class EmailNotification:
    def send(self):
        print("Sending Email Notification")
EmailNotification1 = EmailNotification()
EmailNotification1.send()

"""

class Account:
    def info(self):
        print("Generic Account")
class SavingAccount:
    def info(self):
        print("Savings Account")
class CurrentAccount:
    def info(self):
        print("Current Account")
s1 = SavingAccount()
c1 = CurrentAccount()
s1.info()
c1.info()