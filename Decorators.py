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