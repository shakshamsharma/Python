#super()

#Practice 1
"""
class Person:
    def introduce(self):
        print("I am a person")
class student(Person):
    def introduce(self):
        super().introduce()
        print("I am a Student")
introduce1 = student()
introduce1.introduce()

#Practice 2

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
car1 = Car("BMW", "M5")
print(car1.brand)
print(car1.model)


#Practice 3
class Employee:
    def __init__(self, name):
        self.name = name
class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
dev1 = Developer("Saksham","Python")
print(dev1.name)
print(dev1.language)



#Mini Challenge
class Account:
    def __init__(self, owner):
        self.owner = owner


class SavingsAccount(Account):
    def __init__(self, owner, balance):
        super().__init__(owner)
        self.balance = balance


show = SavingsAccount("Saksham", 5000)

print("Owner:", show.owner)
print("Balance:", show.balance)
        

"""
