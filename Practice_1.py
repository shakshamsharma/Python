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

def largest_number(number):
    largest = number[0]
    for num in number:
        if num > largest:
            largest = num
    return largest
print(largest_number([1,2,7,8,5,95]))