"""

def greet(name):  -> #Multiple Parameter
    print("Hello", name)
greet("Saksham")  -> #Arguement


def add(a, b):  -> #Multiple Parameter
    print(a+b)
add(10, 20)  -> #Arguement



def greet(name="Guest"):  -> #Default Parameter
    print("Hello",name)
greet() -> #calling without an arguement


def power(number, exponent=2):
    return number ** exponent
print(power(5))


#Keyword Arguement

def introduce(name, age):
    print(name, age)
introduce("Saksham",22)


def introduce(name="Saksham", age=22):
    print(name, age)
introduce()


#Return Multiple Values

def calculate(a,b):
    return a+b, a-b
print(calculate(10,20))


def calculate(a, b):
    return a+b,a-b
sum1, diff = calculate(10,20)
print(sum1)
print(diff)
"""

#Practice Question
"""

def greet(name="Guest"):
    print("Hello", name)
greet()


def area(length, width=2):
    return length * width
print(area(10))


def introduce(name = "Saksham", age = 22):
    print(name, age)
introduce()


def introduce(name, age):
    print(name, age)
introduce("Saksham",22)


def operation(a,b):
    return a+b, a-b
print(operation(10,20))

"""

def student(name, course="Python", duration="3 Months"):
    print(name, course, duration)
student(name="Saksham")
