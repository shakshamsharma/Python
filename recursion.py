#Recursion is when a function calls itself.
"""

def count(n):
    if n>5:
        return
    print(n)
    count(n+1)
count(1)

#Reverse
def count(n):
    if n>5:
        return
    count(n+1)
    print(n)
count(1)


#Factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#Sum of all numbers
def count(n):
    if n==1:
        return 1
    return n + count(n-1)
print(count(5))


#Reverse string
def reverse(word):
    if word == "":
        return ""
    return reverse(word[1:])+word[0]
print(reverse('Python'))

"""

#Practice
"""
def count(num):
    if num>5:
        return
    print(num)
    count (num+1)
count(1)


def count(num):
    if num>5:
        return 
    count(num+1)
    print(num)
count(1)
    
def reverse(num):
    if num=="":
        return ""
    return reverse(num[1:])+num[0]
print(reverse('Python'))

 
def factorial(num):
    if num==1:
        return 1
    return num * factorial(num-1)
print(factorial(4))

 
def sum(num):
    if num==1:
        return 1
    return num + sum(num-1)
print(sum(5))
"""


