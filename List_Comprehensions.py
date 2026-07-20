#Normally you write:
"""
numbers = []
for i in range(1,6):
    numbers.append(i*i)
print(numbers)
"""
#List comprehension:
"""
numbers = [i for i in range (1,6)]
print(numbers)
"""
#Square
"""
numbers = [i * i for i in range (1,6)]
print(numbers)
"""
#Convert to uppercase
"""
words = ["Python","Java","c++"]
result = [word.upper() for word in words]
print(result)
"""
#Even Number
"""
even = [i for i in range(1,11) if i%2==0]
print(even)
"""

#odd number
"""
odd = [i for i in range(1,11) if i%2!=0]
print(odd)
"""

#Strings Longer Than 4 Letters
"""
words = ["cat","python","dog","Elephant"]
result = [word for word in words if len(word)>4]
print(result)
"""

#Even → "Even"
#Odd → "Odd"
"""
check = ["Even" if i%2==0 else "Odd" for i in range(1,11)]
print(check)
"""

#Practice - 1
"""
numbers = [i for i in range(1, 6)]
print(numbers)
"""


#Practice - 2
"""

numbers = [10,20,30,40,50]
result = [number * 10 for number in numbers]
print(result)
"""

#Practice - 3
"""
names = ["rahul", "saksham", "amit"]
result = [name.upper() for name in names]
print(result)
"""

#Practice - 4
"""
numbers = [number for number in range(1,20) if number%3==0]
print(numbers)
"""

#Practice - 5
"""
words = ["apple", "hi", "banana", "car", "orange"]
result = [word for word in words if len(word)>4]
print(result)
"""

#Mini Challenge
"""
students = [
    ("Rahul", 80),
    ("Saksham", 95),
    ("Amit", 70),
    ("Priya", 88)
]

result = [student[0] for student in students if student[1]>=80]
print(result)
"""

"""
result = [number * 10 for number in range(1,6)]
print(result)
"""