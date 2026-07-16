#An error that occurs while the program is running.
#Example 1
"""
try:
    num = int(input("Enter the number: "))
    print(num)
except:
    print("Enter the vaild number")
    """
    
#Example 2
"""
try:
    print(10/0)
except ZeroDivisionError:
    print("This is not a valid statement")
    
"""

#Example 3
"""
try:
    num = int("Hello")
except:
    print("Not a valid value")
    """
    
#Example 4 
#Multiple Exceptions
"""
try:
    num = int(input("Enter the number: "))
    result = 100/num
    print(result)
    
except ValueError:
    print("Enter the valid value")
    
except ZeroDivisionError:
    print("Can't divided by zero")
    """
    
#Example 5
#Exception Object
"""
try:
    print(10/0)
except Exception as e:
    print(e)
    """
    
#Example 6 
"""
try:
    num = int("Hello")
    print(num)
except Exception as e:
    print(e)
    """
    
#Example 7 
#With else
"""
try:
    print(100/5)
except:
    print("Enter the valid value")
else:
    print("no error")
    """
    
#Example 8
#Finally
"""
try:
    print(10/2)
except:
    print("Error")
finally:
    print("Program Finished")
    """
    
#Example 9 
#Practice - 1
#Handle division by zero.
"""
try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except:
    print("Cannot divide by zero")
    """
    

#Practice 2
"""
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Value Error")
    """
    
#Practice 3
"""
try:
    numbers = [10,20,30]
    print(numbers[5])
    
except IndexError:
    print("Index Error")
    """
    
#Practice 4
"""
student = {
    "name":"Rahul"
}
try: 
    print(student["age"])
except KeyError:
    print("Key Error")
    """
    
#Mini Challenge
"""
try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid Value")
    """