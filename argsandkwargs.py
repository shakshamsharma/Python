#*args
"""
def add(*numbers):
    print(numbers)
add(10, 20)

def show_name(*names):
    for name in names:
        print(name)
show_name("Saksham","Boogy","Vanshu")
"""

#**wrags
"""
def test(name, **info):
    print(name)
    print(info)
test("Saksham", age='21', city='Palampur')
"""

#Practice
"""
def add(*numbers):
    Total = 0
    for num in numbers:
        Total+=num
    return Total
print(add(10,20,30))


def multiply(*numbers):
    into = 1
    for multiplys in numbers:
        into*=multiplys
    return into
print(multiply(2,3,6))


def show_students(*names):
    for name in names:
        print(name)
show_students("Saksham", "Boogy", "Vanshu")


def profile(name, **info):
    print(name)
    print(info)
profile(
    "Saksham",
    age=22,
    course="Python",
    city="Delhi"
)
"""

def calculate(operation, *numbers):

    if operation == "sum":
        total = 0

        for num in numbers:
            total += num

        return total

    elif operation == "multiply":
        result = 1

        for num in numbers:
            result *= num

        return result

    else:
        return "Invalid"
    
print(calculate("sum", 10, 20, 30))
print(calculate("multiply", 2, 3, 4))
        