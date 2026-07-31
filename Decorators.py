"""
def gift():
    print("Hello")

def run(f):
    f()

run(gift)
"""

"""
def gift():
    print("Hello")

def send(f):
    print("Saksham")
    f()
    print("Sharma")

send(gift)
"""
#Decorators replace one function with another function.

"""
def hello():
    print(10+20)

def bye():
    print("Bye")
    print(10+20)

hello = bye
hello()
"""


"""
def hello():
    print("Hello")

def exceute(func):
    print(10+20)
    func()
exceute(hello)
"""


#Nested Function
"""
def outer():
    print("I am outer")

def inner():
    print("I am inner")

outer()
inner()
"""

"""
def outer():
    print("I am outer")

def inner():
    print("I am inner")

inner()

print("Outer ends")

outer()
"""


"""
def outer():

    def inner():
        print("Hello")

    return inner
"""


"""
def test():

    def hello():
        print("Hello")

    return hello

a = test()
a()
"""


"""
def hello():
    print("Hello")
def run(func):
        def inner():
            print("Starting")
            func()
            print("Ending")
        return inner

hello = run(hello)

hello()
"""

"""
def run(func):
    def inner():
        print("Starting")
        func()
        print("Ending")
    return inner
    
@run
def hello():
    print("Hello")
hello()
"""
"""
def run(func):
    def inner(a,b):
        print("Starting")
        func(a,b)
        print("Ending")
    return inner

@run
def add(a, b):
    print(a + b)
add(10, 20)
"""
"""
def run(func):
    def inner(*args):
        print("Starting")
        func(*args)
        print("Ending")
    return inner

@run
def add(a, b, c):
    print(a + b + c)
add(10, 20, 30)
"""

"""
def zoo(bie):
    def inner(*args):
        print("Starting")
        bie(*args)
        print("Ending")
    return inner 

@zoo
def hello(a,b,c):
    print(a*b*c)
hello(10,20,30)
"""
"""
def show(*args):
    print(args)

show(1, 2)
show()
show("A")
"""

"""
def student(**kwargs):
    print(kwargs)
student(name = "Saksham", age = "21")
"""

"""
def student(func):
    def inner(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Ending")
        return result
    return inner
@student
def hello(name, age):
    print(name)
    print(age)
hello("Saksham", 21)
"""

"""
from functools import wraps
def run(func):
    @wraps(func)
    def inner():
        print("Starting")
        func()
        print("Ending")
    return inner

@run
def hello():
    print("Saksham")
hello()
"""

"""
from functools import wraps
def repeat(times):
    def decorators(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorators

@repeat(3)
def hello():
    print("Saksham")
hello()
"""