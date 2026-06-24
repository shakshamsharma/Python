"""
name = 'Saksham'
print(name[0])

name = 'Saksham'
print(name[-1])
print(name[3])
"""

#Practice
"""
name = 'Computer'
print(name[0])
print(name[7])

language = "Programming"
print(language[0])
print(language[3])
print(language[6])

city = "Mumbai"
print(city[0])
print(city[-1])
print(city[3])



name = input("Enter your name: ")
print(name[0])
print(name[-1])

"""

#SLICING

"""

name = 'Saksham'
print(name[0:6])
    
name = 'Saksham'
print(name[:3])

name = 'Saksham'
print(name[2:])

name = 'Saksham'
print(name[:])

name = 'Saksham'
print(name[-2:])

name = 'Saksham'
print(name[::-1])

"""

#Practice Question

"""
word = 'Computer'
print(word[0:4])
print(word[-5:])

language = "Programming"
print(language[:7])
print(language[-4:])
print(language[3:7])

city = "Mumbai"
print(city[:3])
print(city[-3:])
print(city[0:6])

name = input("Enter your name: ")
print(name[:3])
print(name[-3:])

word = "Python"
print(word[0:6:2])

word = "Developer"
print(word[::-1])

"""


#string + Loops
"""
name = 'Saksham'
for ch in name:
    print(ch)
    
name = 'Saksham'
for ch in name:
    print(ch, end=" ")
    
    
    
name = 'Saksham'
count = 0
for ch in name:
    count += 1
print(count)


name = input("Enter the name: ")
count =0
for ch in name:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels: ",count)


name = 'saksham123'
count = 0 
for ch in name:
    if ch.isdigit():
        count+=1
print(count)



name = 'SaKshaM123'
count = 0 
for ch in name:
    if ch.islower():
        count+=1
print(count)
"""

#Practice
"""
word = 'Computer'
for ch in word:
    print(ch, end=" ")
    print()
    
    

word = "Education"
count = 0
for ch in word:
    if ch in 'aeiouAEIOU':
        count+=1
print("Vowel: ",count)



word = "PyThOnPrOgRaM"
count =0
for ch in word:
    if ch.isupper():
        count+=1
print(count)


text = "abc123xyz45"
count =0
for ch in text:
    if ch.isdigit():
        count=count+1
print(count)


word = "Developer"
reverse = ""
for ch in word:
    reverse = ch + reverse
print(reverse)


name = input("Enter the name to check weather it is palindrome or not: ")
if name == name[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")

"""

sentence = input("Enter a sentence: ")
vowel=0
digit = 0
upper = 0

for ch in sentence:
    if ch in 'aeiouAEIOU':
        vowel +=1
        
    if ch.isdigit():
        digit+=1
    if ch.isupper():
        upper+=1
print(vowel)
print(digit)
print(upper)

                

