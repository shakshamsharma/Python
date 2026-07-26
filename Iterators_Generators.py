#What is an Iterator?
#An iterator is an object that remembers:
#Where it currently is.
#What the next value should be.
"""
numbers = [10,20,30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
"""

#Generator in a for Loop
#It creates values one at a time.
"""
def hello():
    yield "Saksham"
g = hello()
print(next(g))
"""

#With For Loop
"""
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
"""

#iter()
"""
numbers = [10,20,30]
it = iter(numbers)
print(it)
"""

"""
numbers = [10,20,30,40]
it = iter(numbers)
print(next(it))
print(next(it))
"""

"""
def hello():
    yield 1
    yield 2
    yield 3

g = hello()
print(next(g))
"""

"""
def count():
    yield 1
    yield 2
    yield 3

for num in count():
    print(num)
"""

#Practice - 1
"""
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
"""

#Practice - 2
"""
def colors():
    yield "Red"
    yield "Green"
    yield "Blue"
c = colors()
print(next(c))
print(next(c))
print(next(c))
"""

#Practice - 3
"""
def colors():
    yield "Red"
    yield "Green"
    yield "Blue"
for c in colors():
    print(c)
"""

#Practice - 4
"""
def even_numbers():
    yield 2
    yield 4
    yield 6
    yield 8
    yield 10
for i in even_numbers():
    print(i)
"""

#Mini Challenge
"""
def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

for c in countdown():
    print(c)
"""



            

        
