#Lambda
#Examples
"""
square = lambda x: x*x
print(square(5))

add = lambda a,b: a+b
print(add(10, 20))

multiply = lambda a,b: a*b
print(multiply(10,2))

is_even = lambda x: x%2==0
print(is_even(10))
print(is_even(7))
 
is_odd = lambda x: x%2!=0
print(is_odd(10))
print(is_odd(1))

power = lambda a,b: a**b
print(power(2, 3))


students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Amit", 78)
]
students.sort() #sort by name
print(students)


students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Amit", 78)
]
highest = max(students, key= lambda student: student[1])
print(highest)


students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Amit", 78)
    ]
lowest = min(students, key=lambda student: student[1])
print(lowest)


numbers = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)


numbers = [1,2,3,4,5,6,7,8]
square = list(map(lambda x:x*x, numbers))
print(square)

numbers = [1,2,3]

result = list(map(lambda x: x + 1, numbers))

print(result)
"""

#Practice
"""
square = lambda x: x*x
print(square(6))

add = lambda a,b: a+b
print(add(10,20))

is_positive = lambda x: x>0
print(is_positive(10))
print(is_positive(5))


numbers = [1,2,3,4,5]
square = list(map(lambda x:x*x, numbers))
print(square)


numbers = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)


"""

"""
square = lambda x: x*x
print(square(6))

add = lambda a,b: a+b
print(add(10,20))

is_positive = lambda x: x>0
print(is_positive(10))
print(is_positive(5))


numbers = [1,2,3,4,5]
square = list(map(lambda x:x*x, numbers))
print(square)


numbers = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)
"""

students = [
    ("Saksham", 85),
    ("Rahul", 92),
    ("Priya", 88),
    ("Amit", 79)
]
highest = max(students, key =lambda student: student[1])
sorting = sorted(students, key = lambda student: student[1])
find_marks = filter(lambda student: student[1]>85, students)
print(highest)
print(sorting)
print(find_marks)
