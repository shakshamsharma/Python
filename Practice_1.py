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


#Practice - 38
"""
receipts = [
    {"merchant": "Amazon", "amount": "129.99"},
    {"merchant": "Walmart", "amount": "85.00"},
    {"merchant": "Amazon", "amount": "49.50"},
    {"merchant": "Target", "amount": "200.00"}
]
total = 0
for receipt in receipts:
    total += float(receipt["amount"])
print(total)
"""

#Practice - 39
"""
receipts = [
    {"merchant": "Amazon", "amount": "129.99"},
    {"merchant": "Walmart", "amount": "85.00"},
    {"merchant": "Amazon", "amount": "49.50"},
    {"merchant": "Target", "amount": "200.00"}
]
total = 0
for receipt in receipts:
    if receipt["merchant"] == "Amazon":
        total += float(receipt["amount"])
print(total)
"""

#Practice - 40
"""
receipts = [
    {"merchant": "Amazon", "amount": "129.99"},
    {"merchant": "Walmart", "amount": "85.00"},
    {"merchant": "Amazon", "amount": "49.50"},
    {"merchant": "Target", "amount": "200.00"},
    {"merchant": "Walmart", "amount": "15.00"}
]
total = {}
for receipt in receipts:
    merchant = receipt["merchant"]
    amount = float(receipt["amount"])
    if merchant not in total:
        total[merchant]=0
        total[merchant] += amount
print(total)
"""

#Practice - 41
#Sum of Odd Numbers
"""
numbers = [2, 5, 7, 10, 13, 16, 21]
total = 0
for num in numbers:
    if num%2!=0:
        total = total + num
print(total)
"""

#Practice - 42
#Find the First Negative Number
"""
def first_negative(numbers):
    for num in numbers:
          if num < 0:
            return num
print(first_negative([5, 8, 3, -2, 7, -9]))
"""

#Practice - 43
#Count Numbers Greater Than Average
"""
def count_number(numbers):
    total = 0
    count = 0
    count_greater =0
    for num in numbers:
        total = total + num
        count+=1
    average = total/count
    for num in numbers:
        if num > average:
            count_greater+=1
    return count_greater
print(count_number([10, 20, 30, 40, 50]))
"""

#Practice - 44
#Separate Positive and Negative Numbers
"""
numbers = [-3, 5, -8, 10, 2, -1, 7]
positive = []
negative = []
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
print(positive)
print(negative)
"""

#Practice - 45
#Find the Longest Word
"""
words = ["cat", "elephant", "dog", "butterfly", "ant"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
"""

#Practice - 46
#Count Words Starting With a Specific Letter
"""
words = ["apple", "banana", "avocado", "grape", "apricot", "mango"]
count = 0
for word in words:
    if word[0] == 'a':
        count+=1
print(count)
"""

#Practice - 47
#Create a List of Even Numbers
"""
numbers = [1, 4, 7, 8, 11, 12, 15, 20]
even = []
for num in numbers:
    if num%2==0:
        even.append(num)
print(even)
"""

#Practice - 49
#Replace Negative Numbers With 0
"""
numbers = [5, -2, 8, -7, 3, -1, 10]
result = []
for num in numbers:
    if num < 0:
        result.append(0)
    else:
        result.append(num)
print(result)
"""

#Practice - 50
#Count Vowels in Each Word
"""
words = ["apple", "banana", "grape"]
for word in words:
    count = 0
    for char in word:
        if char in 'aeiouAEIOU':
            count+=1
    print(word, count)
"""

#Practice - 51
#Find Common Elements
"""
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9, 2]
common = []
for num in list1:
        if num in list2:
            common.append(num)
print(common)
"""

#Practice - 52
#Count numbers divisible by 3
"""
numbers = [3, 7, 9, 12, 14, 18, 20]
count = 0
for num in numbers:
    if num%3==0:
        count+=1
print(count)
"""

#Practice - 53
#Find the smallest number
"""
numbers = [8, 3, 12, 5, 1, 9]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)
"""

#Practice - 54
#Create a list of numbers greater than 10
"""
numbers = [4, 15, 7, 22, 9, 18, 3]
result = []
for num in numbers:
    if num > 10:
        result.append(num)
print(result)
"""

#Practice - 55
#Count vowels in a string
"""
text = "Programming"
count = 0
for char in text:
    if char in 'aeiouAEIOU':
        count+=1
print(count)
"""

#Practice - 56
#Find the first even number
"""
def even_number(numbers):
    for num in numbers:
        if num%2==0:
            return num
print(even_number([3, 7, 11, 9, 14, 20, 8]))
"""

#Practice - 56
#Find the first even number
"""
numbers = [3, 7, 11, 9, 14, 20, 8]
for num in numbers:
    if num%2==0:
        break
        print(num)
"""

#Practice - 57
#Find the sum of numbers greater than 10
"""
numbers = [4, 15, 7, 22, 9, 18, 3]
total = 0
for num in numbers:
    if num > 10:
        total = total + num
print(total)
"""

#Practice - 58
#Find the longest word's length
"""
words = ["cat", "elephant", "dog", "butterfly"]
largest = len(words[0])
for word in words:
    if len(word) > largest:
        largest = len(word)
print(largest)
"""

#Practice - 59
#Count numbers between 5 and 15
"""
numbers = [2, 5, 8, 12, 16, 7, 20, 14, 3]
count = 0
for num in numbers:
    if num >= 5 and num <= 15:
        count+=1
print(count)
"""

#Practice - 60
#Find the second smallest number
"""
numbers = [8, 3, 12, 5, 1, 9]
smallest = numbers[0]
second = None
for num in numbers:
    if num < smallest:
        second = smallest
        smallest = num
    elif second is None or num < second:
        second = num
print(second)
"""

#Practice - 61
#Find duplicate numbers
"""
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
seen = []
duplicate = []
for num in numbers:
    if num not in seen:
        seen.append(num)
    else:
        duplicate.append(num)
print(duplicate)
"""

#Practice - 62
"""
receipts = [
    {"merchant": "Amazon", "amount": "129.99"},
    {"merchant": "Walmart", "amount": "85.00"},
    {"merchant": "Amazon", "amount": ""},
    {"merchant": "Target", "amount": "200.00"},
    {"merchant": "Amazon", "amount": "49.50"}
]
new_list = []
for receipt in receipts:
    if receipt["merchant"] == "Amazon" and receipt["amount"] != "":
        new_list.append(receipt)
print(new_list)
"""

#Practice - 63
#Handle missing values
"""
receipts = [
    {"merchant": "Amazon", "amount": "129.99"},
    {"merchant": "Walmart", "amount": None},
    {"merchant": "Target", "amount": "200.00"},
    {"merchant": "Amazon", "amount": None},
    {"merchant": "Nike", "amount": "150.00"}
]
total = 0
for receipt in receipts:
    if receipt["amount"] is not None:
        total += float(receipt["amount"]) 
print(total)
"""

#Practice - 64
"""
receipts = [
    {"merchant": "amazon", "amount": "129.99"},
    {"merchant": "WALMART", "amount": "85.00"},
    {"merchant": "Target", "amount": "200.00"}
]
cleaned = []
for receipt in receipts:
    merchant = receipt["merchant"].title()
    amount = float(receipt["amount"])
    cleaned_receipt = {
    "merchant": merchant,
    "amount": amount
}
    cleaned.append(cleaned_receipt)
    print(cleaned)
"""

#Practice - 65
#Find the sum of positive numbers
"""
numbers = [-5, 8, -2, 3, -1, 10, 2]
total = 0
for num in numbers:
    if num > 0:
        total = total + num
print(total)
"""

#Practice - 66
#Count numbers less than 10
"""
numbers = [4, 12, 7, 15, 2, 18, 9]
count = 0
for num in numbers:
    if num < 10:
        count+=1
print(count)
"""

#Practice - 67
#Create a list of odd numbers
"""
numbers = [2, 5, 8, 11, 14, 17, 20]
new_list = []
for num in numbers:
    if num%2!=0:
        new_list.append(num)
print(new_list)
"""


#Practice - 68
#Find the Most Frequent Number
"""
numbers = [1, 2, 2, 3, 1, 2, 4, 2]

frequency = {}

# Step 1: Count how many times each number appears
for num in numbers:

    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Step 2: Find the number with the highest frequency
most_frequent = None
highest_count = 0

for num in frequency:

    if frequency[num] > highest_count:
        most_frequent = num
        highest_count = frequency[num]

print(most_frequent)
"""


#Practice - 69
#Remove all vowels from a string
"""
text = "Programming"
result = ""
for char in text:
    if char not in 'aeiouAEIOU':
        result += char
print(result)
"""

#Practice - 70
#Find the first character that appears twice
"""

text = "programming"
seen = []
for char in text:
    if char in seen:
        print(char)
        break
    else:
        seen.append(char)
"""

#Practice - 71
#Reverse a list without using [::-1]
"""
numbers = [1, 2, 3, 4, 5]
reverse_list = []
for num in numbers:
    reverse_list.insert(0, num)
print(reverse_list)
"""


#Practice - 72
#Remove duplicate elements while preserving order
"""
numbers = [1, 2, 2, 3, 1, 4, 3, 5]
duplicate = []
for num in numbers:
    if num not in duplicate:
        duplicate.append(num)
print(duplicate)
"""


#Practice - 73
#Find the number closest to zero
"""
numbers = [-8, 3, -2, 7, -1, 5]
closest = numbers[0]
for num in numbers:
    if abs(num) < abs(closest):
        closest = num
print(closest)
"""


#Practice - 74
#Check whether a list is sorted in ascending order
"""
numbers = [1, 3, 5, 7, 9]
is_sorted = True
for i in range(len(numbers) -1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break
print(is_sorted)
"""

#Practice - 75
"""
import re
email = """
#Thank you for your purchase from Amazon.
#Order ID: AMZ-847291
#Total: $129.99
"""
result = {}
merchant = re.search(r"purchase from ([A-Za-z]+)", email)
order = re.search(r"AMZ-(\d{6})", email)
total = re.search(r"\$(\d+\.\d{2})", email)
result["merchant"] = merchant.group(1)
result["order"] = order.group(1)
result["total"] = float(total.group(1))
print(result)
"""

#Practice - 76
#Find the largest even number
"""
numbers = [3, 8, 5, 12, 7, 10, 15, 6]
largest = numbers[0]
for num in numbers:
    if num%2==0 and num > largest:
        largest = num
print(largest)
"""

#Practice - 77
#Find the smallest positive number
"""
numbers = [-5, 8, -2, 3, -1, 10, 2]
smallest = None
for num in numbers:
    if num > 0 and smallest is None:
        smallest = num
    elif num > 0 and num < smallest:
        smallest = num
print(smallest)
"""

#Practice - 78
#Count words longer than 5 characters
"""
words = ["cat", "elephant", "dog", "butterfly", "apple", "computer"]
count = 0
for char in words:
    if len(char) > 5:
        count+=1
print(count)
"""

#Practice - 79
#Find the first number greater than the average
"""
numbers = [10, 20, 30, 40, 50]
total = 0
count = 0
for num in numbers:
    count+=1
    total = total+num
average = total/count
for num in numbers:
    if num>average:
        print(num)
        break
"""

#Practice - 80
#Find the longest word that starts with "a"
"""
words = ["apple", "banana", "avocado", "grape", "apricot", "ant"]
longest = ""
for word in words:
    if word[0] == 'a' and len(word) > len(longest):
        longest = word
print(longest)
"""


#Practice - 81
#Count the frequency of each character
"""
text = "banana"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
"""

#Practice = 82
#Find the first non-repeating character
"""
text = "swiss"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
for char in text:
    if frequency[char]==1:
        print(char)
        break
"""

#Practice - 83
#Find the common characters between two strings
"""
text1 = "hello"
text2 = "world"
common = []
for char in text1:
    if char in text2:
        if char not in common:
            common.append(char)
print(common)
"""

#Practice - 84
#Count the number of words containing the letter "a"
"""
words = ["apple", "dog", "banana", "cat", "elephant"]
count = 0
for word in words:
        if 'a' in word:
            count+=1
print(count)
"""

#Practice - 85
#Find the longest consecutive increasing sequence
"""
numbers = [1, 2, 3, 2, 4, 5, 6, 1]

current = 1
longest = 1

for i in range(1, len(numbers)):

    if numbers[i] > numbers[i - 1]:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

print(longest)
"""
