
"""
def greeting():
    print("Hello, How are you")
    print("May god bless you")
greeting()

def message(name):
    print("Hello",name)
message("Saksham")



def add(a, b):
    print(a+b)
add(10, 20)


def add(a, b):
    return(a + b)
result = add(10, 20)
print(result)


def square(num):
    return num * num
result = square(5)
print(result)


def is_even(num):
    return num%2==0
result = is_even(10)
print(result)
"""

#Practice 
"""
def greet():
    print("Welcome to Python")
greet()


def show_name(name):
    print("Hello",name)
show_name("Saksham")


def add(a, b):
    print(a + b)
add(10, 30)

def square(num):
    return num*num
result = square(5)
print(result)

def is_positive(num):
    return num >= 0
result = is_positive(10)
print(result)


#Mini Challenge
def calculator(a, b, operation):
    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b

    else:
        return "Invalid"
print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))
"""