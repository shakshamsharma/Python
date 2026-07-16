#Read file
"""
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
"""
#Write file
"""
file = open("data.txt", "w")
file.write("Always The Great")
file.close()
"""
#Again read after changes
#w deletes old content first.
"""
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
"""
#Append
"""
file = open("data.txt","a")
file.write("\nSaksham The Great")
file.close()
"""
#ReadOneLine
"""
file = open("data.txt","r")
content = file.readline()
print(content)
print(file.readline())
file.close()
"""

#Read All Lines
"""
file = open("data.txt","r")
print(file.readlines())
file.close()
"""

#Loop Through File
"""
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()
"""

#Close File Better way (with)
"""
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    """
    
#Another Example
"""
with open("data.txt","w") as file:
    print(file.write("Saksham"))
    """
    
#close() may never run.
#with open(...) as file:
#Python guarantees cleanup.

#File + Exception Handling
"""
try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")
"""

#PermissionError
#Trying to access protected files.

#IsADirectoryError
#Trying to open a folder as a file.

#Create a new file
"""
file = open("Saksham.txt","x")
print(file.write("Saksham The Great"))
file.close()
"""

#Mini Challange

with open("notes.txt","x") as file:
    print(file.write("Learn Python OOP"))
    print(file.write("\nLearn File Handling"))
    
    

    print(file.read())