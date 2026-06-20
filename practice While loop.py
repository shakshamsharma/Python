"""
n = int(input("Enter your desired number"))
i = 1
while i <= n:
    print(i*"*")
    i = i+1
    """
    
"""
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
    """

"""
name = ''
while name != 'Saksham':
    print("please enter your valid name: ")
    name = input(">")
print("Thanku")

    """
"""
while True:
    print ("Enter you name")
    name = input(">")
    if name == 'Saksham':
        break
print('Thanku')

"""
 

#count down

"""
count = 10
while count >= 1:
    print(count)
    count =  count - 1
print ("Blast OFF")

"""
#Suppose we want the user to keep entering numbers until they type 0.
"""
num = int(input("Enter 0 to stop the loop: "))
while num != 0:
    print("You entered: ", num)
    num = int(input("Enter 0 to stop the loop: "))
    
print("Loop close, thanku")
    
"""
"""
num = 1
total_sum = 0

while num <= 5:
    total_sum += num
    num += 1
    
print(">",total_sum)
"""

"""
num = int(input("Enter the number 0 to stop the loop"))
while num != 0:
    print("Enter again")
    num = int(input("Enter the number 0 or stop"))
print("You escape the loop")
"""


#while if-else
"""
num = 1

while num <= 5:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

    num += 1
    
"""
"""
num = -2
while num <= 2:
    if num >= 0:
        print(num,"Positive number")
    else:
        print(num,"negetive number")
    num += 1
    
    """
    
"""
num = 1
while num <= 10:
    if num%3==0:
        print(num,"Divsible by 3")
    else:
        print(num,"not Divsible by 3")
        
    num += 1
"""
"""
count = 1
while count <= 3:
    num = int(input("Enter the number: "))
    if count%2==0:
        print("even number")
    else:
        print("odd number")
    count +=1
    
"""

#practice 1
"""
num = 1
while num <= 10:
    if num%2==0:
        print(num,"Even number")
    else:
        print(num,"Odd number")
    num += 1
    
"""

#practice 2
"""
num = 1
while num <= 15:
    if num%5==0:
        print(num,"divisible by 5")
    else:
        print(num,"not divisible by 5")
    num += 1
    
"""

#practice 3
"""
num = 1
while num <= 10:
    if num>5:
        print(num, "is greater then 5")
    else:
        print(num, "is equal or less then 5")
    num += 1
    
    """
    
#practice 4
"""
count = 1
while count <= 10:
    num = int(input("Enter five numbers: "))
    if num >= 0:
        print(num," is Positive number")
    else:
        print(num," is negetive number")
    num = num + 1
    """
#mini challenge
"""
num =1 
while num <= 20:
    if num%3==0 and num%5==0:
        print(num, "fizzbuzz")
    elif num%3==0:
        print(num, "fizz")
    elif num%5==0:
        print(num, "Buzz")
    else:
        print(num)
    num+=1
"""

#while with break
"""
num =1 
while num<=10:
    print(num)
    if num == 5:
        break
    num += 1
    """
"""
while True:
    name = input("type exit to stop: ")
    if name == 'exit':
        break
    print("Hello,",name)
print("program close")
"""

"""
secret = 7
while True:
    guess = int(input("Guess the number between 1 to 10 > "))
    if guess == secret:
        print("Correct!")
        break
    print("Not a good Guess")
    
"""

#Practice Question 1
"""
count = 1
while 1 <= 10:
    print(count)
    if count == 7:
        break
    count +=1
    """
    
#Practice 2
"""
while True:
    enter_pass = input("Enter you password >")
    if enter_pass == 'python123':
        print("ACCESS GRANTED!")
        break
    print("ACCESS DENIED, TRY AGAIN")
    """
    
#Practice 3
"""
while True:
    num = int(input("Enter the positive number: "))
    if num < 0:
        print("Negative number entered. Stopping.")
        break
    print("You entered", num)
    """

#Practice 4
""" 
num = 1
while num <= 20:
    print(num)
    if num%9==0:
        print("Found the first multiple of 9")
        break
    num += 1
    """
    
#Initial Balance
"""
balance = 1000

while True:
    print("\n=====ATM Menu=====")
    print("1. Check Balance")
    print("2. Add Balance")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        print("Your available balance is:", balance)

    elif choice == '2':
        amount = int(input("Enter the balance you want to add: "))
        balance += amount
        print("Amount Added")
        print("Now your current balance is:", balance)

    elif choice == '3':
        print("Thank you")
        break

    else:
        print("Invalid")
        
"""

#While with Continue
"""
num = 1
while num <= 5:
    if num == 3:
        num += 1
        continue
    print(num)
    num += 1
    
"""
"""
num = 1
while num <= 10:
    if num%2==0:
        num += 1
        continue
    print(num)
    num += 1
    
    """
    
"""
num = 1
while num <= 10:
    if num % 3 ==0:
        num += 1
        continue
    print(num)
    num += 1
    """
    
#practice question

"""
num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num = num+1
    
"""

#Practice 2
"""
num =1 
while num <= 15:
    if num%4==0:
        num = num+1
        continue
    print(num)
    num = num+1
    
"""

#Practice 3
"""
count = 1

while count <= 5:
    num = int(input("Enter your input: "))

    if num == 0:
        print("Zero is skipped")
        count += 1
        continue

    print("You entered:", num)
    count += 1
    
    """
#Practice 4
"""
num = 1
while num <= 20:
    if num % 2 == 0 or num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1
    
"""

#mini challenge
"""
num = 1
while num <= 30:
    if num%3==0:
        print("fizz")
        num+=1
        continue
    if num%5==0:
        print("Buzz")
        num+=1
        continue
    print(num)
    num+=1
    """
    
#While-else
"""
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("All numbers are printed")
    
        """
        
"""
num =1
while num <= 5:
    if num == 3:
        num +=1
        break
    print(num)
    num += 1
else:
    print("Completed")
"""
"""
secret = "python"
num = 1
while num <= 3:
    key = input("Enter the secret key: ")
    if key == secret:
        num+=1
        print("access valid")
        break
    else:
        print("Access denied")
        
"""
        
numbers = [5, 8, 12, 15, 18, 20]
while numbers == 15:
        print("Found")
else:
        print("not Found")