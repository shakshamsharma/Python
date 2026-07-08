#Classes/Objects/Methods IN OOPS
"""
class Dog():  #Class
    def bark(self):
        print("Whoof Whoof")
dog1 = Dog() #object
dog1.bark() #method

class Cat():
    def meow(self):
        print("Meow")
cat1 = Cat()
cat1.meow()

class Fan():
    def start(self):
        print("Fan Started")
fan1 = Fan()
fan1.start()

class Phone():
    def ring(self):
        print("ringing...")
ring1 = Phone()
ring1.ring()
"""

#__init__()
"""
class student:
    def __init__(self):
        print("Saksham")
student1 = student()


class student:
    def __init__(self, name):
        print(name)
student1 = student("Saksham")


class student:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)
student1 = student("Saksham")
student2 = student("Boogy")
student1.show_name()
student2.show_name()

"""
#Practice
"""
class Dog:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.name)
dog1 = Dog("Boogy")
dog2 = Dog("Julie")
dog1.show_name()
dog2.show_name()
        
    
class Car():
    def __init__(self, name):
        self.name = name
    def show_brand(self):
        print(self.name)
car1 = Car("BMW")
car2 = Car("Mercedez")    
car1.show_brand()
car2.show_brand()



#Mini Challenge

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
mobile1 = Mobile("Samsung", 50000)
mobile2 = Mobile("Apple", 120000)
mobile1.show_details()
mobile2.show_details()

"""

class student:
    def __init__(self):
        print("Saksham the great")
student1 = student()
