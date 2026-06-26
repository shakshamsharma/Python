#Practice
"""
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(numbers[2])


cities = ["Delhi", "Mumbai", "Chennai", "Pune"]
print(cities[0])
print(cities[-1])
print(cities[1])


fruits = ["Apple", "Banana", "Mango"]
fruits[1] = 'Grapes'
print(fruits)


numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
print(numbers[0:3])
print(numbers[3:6])
print(numbers[::-1])


names = ["Saksham", "Rahul", "Priya"]
for name in names:
    print(name)
    
"""

#List Methods
#Practice

"""
numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)
print(numbers)

numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)


numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
numbers.pop()
print(numbers)


numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))
print(numbers.index(1))


fruits = ["Apple", "Banana", "Mango"]
fruits.reverse()
print(fruits)

items = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print(item, "Added")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in items:
            items.remove(item)
            print(item, "Removed")
        else:
            print("Item not found")

    elif choice == "3":
        print(items)

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
    
    """

#2D Loop
"""
matrix = [
[1, 2, 3],
[4 ,5, 6],
[7, 8, 9]
]
print(matrix[2][2])



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
matrix[0][2] = 90
print(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
for row in matrix:
    print(row)
    

    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
for row in matrix:
    for rows in row:
        print(rows, end=" ")
    print()
    
    
students = [
    ["Saksham", 70],
    ["Vanshu", 80],
    ["Boogy", 90]
    ]
for student in students:
    for classes in student:
        print(classes, end=" ")
    print()
    """
    
#Practice Question
"""
matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(matrix[0])
print(matrix[1])
print(matrix[2])


matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(matrix[0][1])
print(matrix[1][2])
print(matrix[2][1])


matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
matrix[1][1] = 500
print(matrix)


matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
for rows in matrix:
    for row in rows:
        print(row, end=" ")
    print()
    

students = [
    ["Saksham", 85],
    ["Rahul", 90],
    ["Priya", 88]
]
for student in students:
    print(student[0], student[1])
    
    """
    
marks = [
    [85, 90, 88],
    [78, 92, 80],
    [95, 87, 91]
]
for student in marks:
    total = 0

    for mark in student:
        total += mark

    print(total)
