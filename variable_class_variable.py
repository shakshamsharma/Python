#Instance Variables
#These belong to one specific object.

#Class Variables
#These belong to the class itself and are shared by all objects.
"""
class Student:
    School = 'ABC School'
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)
student1 = Student('Saksham')
student2 = Student("Boogy")
student1.show_name()
print(student1.School)
student2.show_name()
print(student2.School)


class Employee:
    Company = 'Microsoft'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_name(self):
        print("Employee name", self.name)
        print("Employee salary", self.salary)
employee1 = Employee('Saksham', 100000)
employee2 = Employee('Boogy', 200000)
employee1.show_name()
print(employee1.Company)
employee2.show_name()
print(employee2.Company)


#Mini Challenge

class Mobile:
    Catagory = "SmartPhone"
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print("Mobile Brand: ",self.brand)
        print("Mobile Price: ",self.price)
mobile1 = Mobile("Samsung", 50000)
mobile2 = Mobile("Apple", 120000)
mobile1.show_details()
print(mobile1.Catagory)
mobile2.show_details()
print(mobile2.Catagory)
"""