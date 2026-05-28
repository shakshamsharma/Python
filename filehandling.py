#File handling
#'r' open for reading
#'w' open for writing
#'x' create a new file and open it for writing
#'a' open for the writing, appending to the end of the file
#'b' binary mode
#'t' text mode
#'+' open a disk file for updating(reading and writing) like r+, w+, a+

"""
f = open("file.txt","r")
data = f.read()
print(data)
f.close()   
"""

#read only particular set of letters
"""
f = open("file.txt","r")
data = f.read(2)
print(data)
f.close()
"""

"""
f = open("file.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()
"""

"""
f = open("file.txt","r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close()
"""

#writing to a file
"""
f = open("file.txt","w")
f.write("Boogy man")

f.close()
"""

#Append
"""
f = open("file.txt","a")
f.write("\nBoogy man")

f.close()
"""

#Automatic create a new file
"""
f = open("demo.txt","w")
f.close()
"""

#r+ Is writes at starting of the file
"""
f = open("file.txt","r+")
f.write("abc")
print(f.read())
f.close()
"""

#It come in truncated so all file data will be clear
"""
f = open("file.txt","w+")
print(f.read())
f.close()
"""

"""
f = open("file.txt","a+")
print(f.read())
f.write("abc")
f.close()
"""

#r+ pointer at starting
#w+ truncate file data will delete
#a+ pointer at ending

#with syntax
#with automatically close the file so no need of closing the file
"""
with open("file.txt","r") as f:
    data = f.read()
    print(data)
    
with open("file.tx","w") as f:
    f.write("xyz")
"""

#Practice Replace the text

"""
with open("practice.txt","w") as f:
    f.write("Hey everyone,\nSaksham this side\n")
    f.write("and I am good")
    
#this will not change in file
with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("good", "fine")
    print(new_data)
    
#this will change in file
with open("practice.txt","w") as f:
    f.write(new_data)
    
"""
    
#find Saksham is there in this file
"""
with open("practice.txt","r") as f:
    data = f.read()
    if (data.find("xsaksham") != -1):
        print("found")
    else:
        print("not found")
        
"""
with open("number.txt","r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    print(nums)