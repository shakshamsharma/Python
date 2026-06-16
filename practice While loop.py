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

num = 1
total_sum = 0

while num <= 5:
    total_sum += num
    num += 1
    
print(">",total_sum)