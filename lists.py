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
"""

items = []
while True:
    print("\n1.Add your item")
    print("2.Remove your item")
    print("3.Show items list")
    print("4.Exit")
    choice = input("Add your choice: ")
    if choice == "1":
        item = input("Enter the item: ")
        items.append(item)
        print(item, "Added")
    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in items:
            items.remove(item)
            print(item, "Removed")
    elif choice == "3":
        print(items)
    elif choice == "4":
        print("GoodBye")
        break
    else:
        print("Invalid")
        
    
    