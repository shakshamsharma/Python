#Abstraction → Hide implementation details
#Show what to do, hide how it works.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Whoof")
class Cat(Animal):
    def sound(self):
        print("Meow")
        
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
"""

#Practice -1 
"""
from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car Starting")
        
class Bike(Vehicle):
    def start(self):
        print("Bike Starting")
        
car = Car()
bike = Bike()

car.start()
bike.start()
"""

#Practice -2
"""
from abc import ABC, abstractmethod
class Employee:
    @abstractmethod
    def work(self):
        pass
    
class Developer(Employee):
    def work(self):
        print("Writing Code")
        
class Designer(Employee):
    def work(self):
        print("Creating Designs")
        
developer = Developer()
designer = Designer()
developer.work()
designer.work()
"""

#Practice -3
"""
from abc import ABC, abstractmethod
class Notification:
    @abstractmethod
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print("Sending Email")
        
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")
        
notification = EmailNotification()
notification1 = SMSNotification()
notification.send()
notification1.send()

"""

#Mini Challange
"""
from abc import ABC, abstractmethod
class BankAccount:
    @abstractmethod
    def withdraw(self):
        pass
    
class SavingsAccount(BankAccount):
    def withdraw(self):
        print("Savings Withdrawal")
    
class CurrentAccount(BankAccount):
    def withdraw(self):
        print("Current Withdrawal")
        
account = SavingsAccount()
account1 = CurrentAccount()

account.withdraw()
account1.withdraw()
"""
