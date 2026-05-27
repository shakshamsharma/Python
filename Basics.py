# Print In Python

"""
name = "Saksham"
age = 21
print("name:",name,"\n","age:", age)
"""

"""
name = "Saksham"
age = 21

name = "Saksham Sharma"
age = 22

print(name)
print(age)
"""


#VARIABLES IN PYTHON

"""
Strings: It is a work like : Saksham
Integer: It is a number like : 21
Float: Its is a Decimal number like : 21.5
Boolean: It is a True or False value
"""

"""
name = "Tony"
last_name = "Stark"
age = 51
is_tony_genius = True

print(name,""+last_name)                          
print(age)
print(is_tony_genius)
"""

"""
first_name = "Tony"
last_name = "Stark"
age = 51
is_tony_genius = True

print("He is",first_name,""+last_name,"and he is",age,"years old and he is a",is_tony_genius,"genius")  
"""

#Input In Python

"""
name = input("What is your name?")
age = input("What is your age?")
print(name)
print(age)
"""

#Excercise 

"""
name = input("Hey kid, what is your superhero name?")
print("Wow! Your superhero name is",name)
here_name = input("Which hero is he?")
print("oh! He is",here_name)
"""

#Type Conversion

"""
old_age= input("what is your old age: ")
int(old_age)
new_age = int(old_age) +2
print(new_age)
"""

#int to float

"""
number = 18
print(float(number))
"""

#Print sum of 2 numbers
"""
first_number = input("Enter your first number: ")
second_number = input("Enter you second number: ")
#print(first_number + second_number)
#sum = first_number + second_number
#print(sum)
#because it is still string and get concatinate
sum = int(first_number) + int(second_number)
#print(sum)
print("The sum is: ",str(sum))
"""

#STRING
"""
name = "saksham"
print(name.upper())
"""

"""
name = "SAKSHAM"
print(name.lower())
"""

"""
name = "Saksham"
print(name.find('s'))
print(name.replace("Saksham", "Saksham The Great"))
print(name.replace("S", "B"))
"""

"""
name = "Saksham Sharma"
print("Z" in name)
"""

#ARITHMETIC OPERATORS

"""
print(5+2)
print(5-2)
print(5/2)
print(5%2)
print(5//2) # by using double // we can remove decimal number after point
print(5**2) #to check the power
"""

"""
num = (2+3*5)
print(num)

num = (2+3) *5
print(num)
"""

"""
print(3>2)
print(3<2)
print(3>=2)
print(3<=2)
print(3==2)
print(3==3)
print(3!=2)
print(not 3 > 2)
"""

#IF elif else statement

"""
age = 2
if(age >= 18):
    print("You can Vote")
elif(age < 18 and age > 3):
    print("You are not a adult")
else:
    print("next time")
print("ThankYou")
"""

#EXCERCISE CALCULATOR
    
"""
First_number = input("Enter your 1st number: ")
operator = input("Enter the operator (+,-,/,*,%): ")
Second_number = input("Enter your 2nd number: ")

First_number = int(First_number)
Second_number = int(Second_number)

if operator == "+":
    print(First_number + Second_number)
    
elif operator == "-":
    print(First_number - Second_number)
    
elif operator == "/":
    print(First_number / Second_number)
    
elif operator == "*":
    print(First_number * Second_number)
    
elif operator == "%":
    print(First_number % Second_number)
    
else:
    print("Invalid")
     
"""

#RANGE 

"""
numbers = range(3)
print(numbers)
"""


#LOOPS

#WHILE LOOP (Jab Tak)

"""
i = 1
while i <= 100:
    print(i)
    i = i+1
"""

"""
i = 1
while (i <= 5):
    print(i * "*")
    i = i +1
"""

"""
i = 5
while (i >= 0):
    print(i * "*")
    i = i -1
"""

#FOR LOOP
"""
for i in range(10):
  print(i)
"""

"""
for x in "banana":
  print(x)
"""

#LIST DATATYPE

"""
marks = [90, 95, "Hundred"]
print(marks)
"""

"""
marks = [90, 95, "Hundred"]
print(marks[0])

marks = [90, 95, "Hundred"]
print(marks[-1])

marks = [90, 95, "Hundred"]
print(marks[0:2])
"""

"""
marks = [90, 95, "Hundred"]
for score in marks:
    print(score)
"""

"""
marks = [90, 95, "Hundred"]
marks.append(100)
print(marks)

marks = [90, 95, "Hundred"]
marks.insert(1, 100)
print(marks)

marks = [90, 95, "Hundred"]
marks.append(100)
print(99 in marks)

marks = [90, 95, "Hundred"]
marks.append(100)
print(len(marks))
"""

#LIST FOR WHILE 

"""
marks = [90, 92, 95, 100]
i = 0
while i < len(marks):
    print(marks[i])
    i = i+1

marks.clear()
print(marks)
"""

#BREAK & CONTINUE

"""
names = ["Ram" ,"sita", "krishna", "Radha"]
for name in names:
    if name == "krishna":
        continue
    print(name)
    
names = ["Ram" ,"sita", "krishna", "Radha"]
for name in names:
    if name == "krishna":
        break
    print(name)
"""

#TUPLES

"""
marks = (90, 92, 95, 97, 97, 97)
print(marks.count(97))

marks = (90, 92, 95, 97, 97, 97)
print(marks.index(97))
"""

#SET - unordered

"""
marks ={90, 92, 95, 97, 97}
for sum in marks:
    print(sum)
"""

#Dictonairy - store as key & value

"""
marks = {"English" : 95, "Physics" : 90}
print(marks["Physics"])
marks["Physics"] = 99
print(marks["Physics"])
"""

#FUNCTIONS

#InBuiltFunctions
"""
int()
str()
bool()
"""

#Module Function

"""
import math
print(dir(math))
"""

"""
from math import sqrt
print(sqrt(16))

from math import *
print(sqrt(16))
"""

#USER DEFINED FUNCTION
def print_sum(first, second=4):
    print(first + second)
    print_sum(1)