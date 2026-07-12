"""
class Animal:
    def sound(self):
        print("Animal Sounds")
class Dog(Animal):
    def sound(self):
        print("Whoof Whoof")
class Cat(Animal):
    def sound(self):
        print("Meow Meow")
        
dog1 = Dog()
dog1.sound()
cat1 = Cat()
cat1.sound()


class Dog():
    def bark(self):
        print("Whoof Whoof")

class Cat():
    def meow(self):
        print("Meow Meow")

class Tiger():
    def roar(self):
        print("Roar Roar")
        
dog1 = Dog()
cat1 = Cat()
tiger1 = Tiger()
dog1.bark()
cat1.meow()
tiger1.roar()

"""
"""
#Practice1
class Shape:
    def draw(self):
        pass
    
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
        
class Square(Shape):
    def draw(self):
        print("Drawing Square")
        
class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")
        
Shape = [Circle(), Square(), Triangle()]
for shapes in Shape:
    shapes.draw()


#Practice 2
class Employee:
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("Writing Code")
class Designer(Employee):
    def work(self):
        print("Creating Designs")
class Tester(Employee):
    def work(self):
        print("Testing Software")
Employee = [Developer(), Designer(), Tester()]
for employees in Employee:
    employees.work()
    """
    
#Practice 3
class Notification:
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print("Sending Email")
        
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")
        
class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")
        
EmailNotification1 = EmailNotification()
SMSNotification1 = SMSNotification()
PushNotification1 = PushNotification()

EmailNotification1.send()
SMSNotification1.send()
PushNotification1.send()

"""
#Mini Challenge
class Transport:
    def move(self):
        pass
    
class Car(Transport):
    def move(self):
        print("Car is Driving")
        
class Plane(Transport):
    def move(self):
        print("Plane is Flying")
        
class Boat(Transport):
    def move(self):
        print("Boat is Sailing")
        
Transport = [Car(), Plane(), Boat()]
for transports in Transport:
    transports.move()
    """