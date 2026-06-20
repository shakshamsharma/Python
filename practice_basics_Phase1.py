"""
present_year = 2026
year = int(input("Enter you data of birth: "))
print(present_year - year,"is your present age")
if year == 2030:
    print("invalid birth year")
    
    """
    
"""  
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight/height**2
print(bmi)
if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")
    
"""  
        
        

"""  
kilometer = int(input("Enter the kg number: "))
print(kilometer*1000,"in meter")

"""

"""
celsius = float(input("Enter the Celsius: "))
F = (celsius * 9/5) + 32
print(F)

"""
"""
ruppee = int(input("Enter the ruppee: "))
convert = (ruppee*100)
print(convert)
"""

#Restaurant Bill 
customer_name = input("Enter your name:             ")
food_item_name = input("Enter your item:            ")
food_quantity = int(input("Enter the food quantity: "))
item_price = int(input("Enter the item price:       "))
subtotal = food_quantity * item_price
print("=====RESTAURANT BILL=====")
print(customer_name)
print(food_item_name)
print(subtotal)
GST = subtotal * 5 / 100
print("GST is:",                                   GST)
final_amount = subtotal + GST
print("Your Final Amount: ",              final_amount)
