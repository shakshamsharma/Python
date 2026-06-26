#Tuple
"""
numbers = (10,20,30,40)
print(numbers[0])
print(numbers[-1])

numbers = (10,20,30,40,50)
print(numbers[1:4])

numbers = (1,2,2,3,2)
print(numbers.count(2))
print(numbers.index(3))

"""
#Dictionary
"""
student = {
    "name": "Saksham",
    "age": 22,
    "marks": 90
}
print(student["name"])

student = {
    "name": "Saksham",
    "age": 22,
    "marks": 90
}
print(student["name"])

student = {
    "name": "Saksham",
    "age": 22,
    "marks": 90
}
student["city"] = "Himachal"
student["marks"] = 100
print(student)

student = {
    "name": "Saksham",
    "age": 22,
    "marks": 90
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("print"))


student = {
    "name": "Saksham",
    "age": 22,
    "marks": 90
}
for key, in student:
    print(key)
    
    
student = {
    "name": "Saksham",
    "age": 22,
    "marks": 90
}
for key, value in student.items():
    print(key, value)
"""
#Practice Dic
"""
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 88
}
print(student["name"])
print(student["marks"])


student = {
    "name": "Rahul",
    "age": 21,
    "marks": 88
}
student["city"] = "Mumbai"
print(student)


student = {
    "name": "Rahul",
    "age": 21,
    "marks": 88
}
student["marks"] = 95
print(student)

student = {
    "name": "Rahul",
    "age": 21,
    "marks": 88
}
print(student.keys())
print(student.values())

student = {
    "name": "Rahul",
    "age": 21,
    "marks": 88
}
student["city"] = "Mumbai"
print(student)
for key, value in student.items():
    print(key, value)
    
    """
    
#Mini Challenge
employee = {
    "name": "Saksham",
    "salary": 50000,
    "department": "IT"
}
choice = input("Which information do you want?")
if choice == 'Salary':
    print(employee.get("salary"))
elif choice == 'Name':
    print(employee.get("name"))
elif choice == 'Department':
    print(employee.get("department"))
else:
    print("Invalid")