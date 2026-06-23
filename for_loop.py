#For loop
"""
for i in range(6):
    print(i)
    """
    
"""
for i in range(1, 6):
    print(i)
    """
    
"""
for i in range(1,20,3):
    print(i)
    """
    
#Practice 1
"""
for i in range(1, 11):
    print(i)
    """

"""  
for i in range(2, 21, 2):
    print(i)
    
"""

"""
for i in range(10, 0, -1):
    print(i)
    """
    
"""
for i in range(1, 11):
    print(5*i)
    """
    
"""
num = int(input("Enter your number: "))
for i in range(1, 11):
    print(num,"*",i,"=",num*i)
    """
    
#for - if-else
"""
for i in range(1, 11):
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")
        
        """
        
"""
for i in range(1, 16):
    if i%5==0:
        print(i,"Divisible by 5")
    else:
        print(i,"Not Divisible by 5")
        
        """
        
"""
for i in range(1, 11):
    if i > 5:
        print(i,"Greater than 5")
    else:
        print(i,"Less than or equal to 5")
        
        """
        
"""
for i in range(1, 21):
    if i%2==0 and i%3==0:
        print(i,"Divisible by both 2 and 3")
    else:
        print(i,"Not divisible by both")
        
        """
      
"""
for i in range(1, 21):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        """
        
#for - break
"""
for i in range(1, 11):
    print(i)
    if i == 7:
        break
        
        """
    
"""
for i in range(1, 21):
    if i%4==0:
        print("found:",i)
        break
    """
    
"""
for i in range(10, 0, -1):
    print(i)
    if i == 5:
        break
"""

"""
secret = 8
for attempt in range(5):
    attempt = int(input("Guess the number: "))
    if attempt == secret:
        print("correct guess")
        break
    else:
        print("wrong guess")
        """

""" 
products = ["Mouse", "Keyboard", "Monitor", "Laptop", "Speaker"]
for product in products:
    if product == 'Laptop':
        print("Product found")
        break
    """
    
#for - continue
#practice 1
"""
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
    """
    
"""
    
for i in range(1, 20):
    if i%4==0:
        continue
    print(i)
    
"""

"""
for i in range(1, 15):
    if i%2!=0:
        continue
    print(i)
    """
    
"""
for i in range(1,20):
    if i%2==0 or i%3==0:
        continue
    print(i)

"""

#mini challenge
"""
items = ["Milk", "Eggs", "Chocolate", "Bread", "Chocolate", "Juice"]
for item in items:
    if item == "Chocolate":
        continue
    print(item)
    """
    
#for - else
#practice
"""
for i in range(1, 6):
    print(i)
else:
    print("Loop Completed")
    """
    
"""
for i in range(1, 6):
    print(i)
else:
    print("Loop Completed")
    """
    
"""
for i in range(1, 10):
    if i == 6:
        print(i)
        break
    else:
        print("Loop Finished Normally")
        """
        
"""
        
numbers = [5, 8, 12, 15, 18, 20]
for number in numbers:
    if number == 15:
        print("found")
    else:
        print("Not found")
        """
        
"""
courses = ["Java", "C++", "JavaScript"]
for course in courses:
    if course == 'Python':
        print("not found")
        break
    else:
        print("found")
        """
        
        
        
"""
secret = "python123"
for attempt in range(3):
    guess = input("take a guess: ")
    if guess == secret:
        print("Correct one!")
        break
    else:
        print("Not correct")
        
"""
"""
for i in range(1, 10):
    if i == 6:
        print(i)
        break
else:
    print("Loop Finished Normally")

"""
        
"""
for i in range(1, 6):
    print(i)
else:
    print("Loop Completed")
    """
    
"""
for i in range(1, 10):
    if i == 6:
        print(i)
        break
    else:
        print("Loop Finished Normally")
        """
        
"""
        
numbers = [5, 8, 12, 15, 18, 20]
for number in numbers:
    if number == 15:
        print("found")
    else:
        print("Not found")
        """
        
"""
courses = ["Java", "C++", "JavaScript"]
for course in courses:
    if course == 'Python':
        print("not found")
        break
    else:
        print("found")
        """
        
        
        
"""
secret = "python123"
for attempt in range(3):
    guess = input("take a guess: ")
    if guess == secret:
        print("Correct one!")
        break
    else:
        print("Not correct")
        """
"""
for i in range(1, 6):
    print(i)
else:
    print("Loop Completed")
    """
    
"""
for i in range(1, 10):
    if i == 6:
        print(i)
        break
    else:
        print("Loop Finished Normally")
        """
        
"""
        
numbers = [5, 8, 12, 15, 18, 20]
for number in numbers:
    if number == 15:
        print("found")
    else:
        print("Not found")
        """
        
"""
courses = ["Java", "C++", "JavaScript"]
for course in courses:
    if course == 'Python':
        print("not found")
        break
    else:
        print("found")
        """
        
        
        
"""
secret = "python123"
for attempt in range(3):
    guess = input("take a guess: ")
    if guess == secret:
        print("Correct one!")
        break
    else:
        print("Not correct")
        
"""
        
"""  
numbers = [5, 8, 12, 15, 18, 20]
for number in numbers:
    if number == 15:
        print("found")
        break
else:
    print("Not found")
        
        """

"""
courses = ["Java", "C++", "JavaScript"]
for course in courses:
    if course == 'Python':
        print("found")
        break
else:
    print("not found")
    """
        
        
"""
secret = "python123"
for attempt in range(3):
    guess = input("take a guess: ")
    if guess == secret:
        print("Correct one!")
        break
    print("Wrong Password")
else:
    print("Not correct")
        
"""

#Nested for Loops
#A Loop Inside Another Loop.

"""
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
        
        """
        
"""
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
    """
    
"""
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end=" ")
    print()
    """
    
"""
for i in range(1, 4):
    for j in range(1, 4):
        print(i*j, end=" ")
    print()
    """
    
"""
for i in range(1):
    for j in range(1, 5):
        print("*", end=" ")
    print()
    
"""

"""
for i in range (6, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
"""


"""
for i in range(6, 0, -1):
    for j in range(1, i-1):
        print("*", end=" ")
    print()
    
"""

"""
for i in range(1, 6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
        
    """
    
"""
for i in range(1, 5):
    for j in range(4-i):
        print(" ", end="")
    for j in range(i):
        print("*",end=" ")
    print()
    
"""

"""
for i in range(6, 0, -1):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i):
        print("*",end=" ")
    print()
    
    """
    
"""
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(i):
        print(i, end=" ")
    print()
    
"""

"""
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j, end=" ")
    print()
    
    """
    
"""
for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()
"""

"""
for i in range(1, 3):
    for j in range(1, 3):
        print(i+j,end=" ")
    print()
    
    """
    
for i in range(1, 4):
    for j in range(1, 4):
        print(j,end=" ")
        
    print()
    

