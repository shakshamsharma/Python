#Practice - 1
"""
count = 0
for num in [1,2,3,4,5]:
    if num%2==0:
        count = count +1
print(count)
  """

#Practice - 2
"""
def count_even(numbers):
    count = 0
    for num in numbers:
        if num%2==0:
            count=count+1
    return count
"""

#Practice - 3
"""
number = [1,2,3,4,5,6]
largest_number = max(number)
print(largest_number)
"""

#Practice - 4
"""
numbers = [1,4,3,6,9]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)
"""

#Practice - 5
"""
def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
"""

#Practice - 6
"""
text = ["python"]
reversed_text = "y" + "p" + "t" + "h" + "o" + "n"
print(reversed_text)
"""

#Practice - 7
"""
text = "Python"
print(text[::-1])
"""

#Practice - 8
"""
text = "Python"
reverse_text = ""
for char in text:
    reverse_text = char + reverse_text
print(reverse_text)
"""

#Practice - 9
"""
def reverse(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text
print(reverse("python"))
"""

#Practice - 10
"""
vowel = "banana"
count = 0
for vow in vowel:
    if vow in 'aeiou':
        count+=1
print(count)
"""

#Practice - 11
"""
def count_vowel(vowel):
    count = 0
    for vow in vowel:
        if vow in 'aeiou':
            count += 1
    return count
print(count_vowel("Banana"))
"""

#Practice - 12
"""
text = "AeIu"
for char in text:
    if char.lower() in 'aeiou':
        print(char)
"""

#Practice - 13
"""
text = "AeIu"
for char in text:
    if char in 'aeiouAEIOU':
        print(char)
"""

#Practice - 14
"""
number = [-1,-2,-3,8,-9,4]
total = 0
for num in number:
    if num > 0:
        total = num + total
print(total)
"""

#Practice - 15
"""
def count_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total = num + total
    return total
print(count_positive([1,-2,5,-8,9]))
"""

#Practice - 16
"""
numbers = [8, 3, 10, 2, 6]
smallest_number = min(numbers)
print(smallest_number)
"""

#Practice - 17
"""
number = [8,4,3,7,5,2]
smallest = number[0]
for num in number:
    if num < smallest:
        smallest = num
print(smallest)
"""

#Practice - 18
"""
def smallest_num(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(smallest_num([4,3,6,8,9]))
"""

#Practice - 19
"""
numbers = [-1,-2,-3,-4,5,6]
count = 0
for num in numbers:
    if num > 0:
        count = count + 1
print(count)
"""

#Practice - 20
"""
def count_postive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count = count + 1
    return count
print(count_postive([-1,2,3,4,-6,7]))
"""

#practice - 21
"""
number = [1,3,5,7,8,9,10]
count = 0
for num in number:
    if num%2==0:
        count = count + 1
print(count)
"""

#Practice - 22
"""
def first_even_number(numbers):
    for num in numbers:
        if num%2==0:
            return num
print(first_even_number([1,3,5,8,9,10]))
"""

#Practice - 23
"""
def count_text(text):
    count = 0
    for char in text:
        if char == 'a':
            count+=1
    return count
print(count_text("Banana"))
"""

#Practice - 24
"""
def count_character(text):
    count = 0
    for char in text:
        count+=1
    return count
print(count_character("banana"))
"""

#Practice - 25
"""
def first_character(text):
    for char in text:
        return char
print(first_character("Python"))
"""

#Practice - 26
"""
text = "Python"
count = 0
for char in text:
    count += 1
    if count == 2:
        print(char)
"""

#Practice - 27
"""
numbers = [1, 4, 7, 8, 11, 12, 15]
count = 0
for num in numbers:
    if num%2!=0:
        count += 1
print(count)
"""

#Practice - 28
"""
numbers = [1, 2, 4, 7, 10, 13, 16]
total = 0
for num in numbers:
    total = total + num
print(total)
"""

#Practice - 29
"""
numbers = [1, 2, 4, 7, 10, 13, 16]
total = 0
for num in numbers:
    if num%2==0:
        total = total + num
print(total)
"""

#Practice - 30
"""
numbers = [4, 12, 7, 15, 20, 3, 11]
count = 0
for num in numbers:
    if num > 10:
        count=count+1
print(count)
"""

#Practice - 31
#find the smallest positive number
"""
def smallest_positive_number(numbers):
    smallest = None
    for num in numbers:
        if num > 0 and (smallest is None or num < smallest):
            smallest = num
    return smallest
print(smallest_positive_number([1,-4,-2,7,2,-9]))
"""

#Practice - 32
#Biggest Even number
"""
def biggest_even_number(numbers):
    largest = None
    for num in numbers:
        if num%2!=0:
            continue
        if largest is None or num > largest:
            largest = num
    return largest
print(biggest_even_number([1,5,3,7,3,14]))
"""

#Practice - 33
#Calculate Average
"""
def average_number(numbers):
    total = 0
    count = 0
    for num in numbers:
        total = total + num
        count = count + 1
        average = total/count
    return average
print(average_number([10,20,30,40,50,60,70]))
"""

#Practice - 34
#Count Uppercase Characters
"""
def upperCase(text):
    count = 0
    for char in text:
        if char.isupper():
            count+=1
    return count
print(upperCase("PyThOn"))
"""

#Practice - 35
#Count Digits
"""
def count_digit(text):
    count = 0
    for digit in text:
        if digit.isdigit():
            count+=1
    return count
print(count_digit("Python123Code45"))
"""

#Practice - 36
#Remove Duplicates
"""
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
"""


#Practice - 37
#Second Largest Number
"""
def second_largest(numbers):
    largest = numbers[0]
    second = None
    for num in numbers:
        if num > largest:
            largest = num
        elif second is None or num > second:
            second = num
    return second
print(second_largest([10, 5, 8, 20, 15]))
"""


    

