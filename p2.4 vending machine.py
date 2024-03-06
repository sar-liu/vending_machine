#programmer: Sarah Liu
#description: 2.4- complete coffee vending machine 
#date: 11/10/23 

print("Welcome to the Coffee-O-Matic 6000, the premier coffee vending machine!!\n")
print("----- Drink Menu -----")
print("1. Espresso \t (Small $1.75, Medium $3.50, Large $5.25)") 
print("2. Americano \t (Small $1.75, Medium $3.50, Large $5.25)")
print("3. Cafe au Lait  (Small $3.75, Medium $7.50, Large $11.25)") 
print("4. Latte \t (Small $2.75, Medium $5.50, Large $8.25)")
print("5. Mocha \t (Small $2.75, Medium $5.50, Large $8.25)\n")

drink = input("Please enter the name of your drink choice: ")
drink=drink.lower()


if drink =="espresso" or drink =="americano":
    print ("You have selected a", drink, "- what a great choice!!\n")
    small_price= 1.75
elif drink =="cafe au lait":
    print ("You have selected a", drink, "- what a great choice!!\n")
    small_price= 3.75
elif drink =="latte" or drink =="mocha":
    print ("You have selected a", drink, "- what a great choice!!\n")
    small_price= 2.75
else:
    print ("Error: Invalid selection.\n")
    exit()

size_selected= input("Please your drink size letter: S (Small), M (Medium), or L (Large): ")
size_selected=size_selected.upper()
if size_selected == "L":
    print ("You have ordered a large drink.")
    price_multiplier = 3
elif size_selected == "M":
    print ("You have ordered a medium drink.")
    price_multiplier = 2
elif size_selected =="S":
    print ("You have ordered a small drink.")
    price_multiplier = 1
else:
    print ("Error: Invalid drink size.")
    exit()

total_price = small_price*price_multiplier
print("Your drink will be $", total_price)
payment= float( input("\nPlease insert payment: $ ") )
payment = round(payment,2)

print ("Payment collected: $ ", payment)
if payment < total_price:
    print("Insufficient funds. Sale has been cancelled.")
    exit()
elif payment == total_price:
    print("Change due: $ 0.00. \nThank you, enjoy your coffee!")
elif payment > total_price:   
    print("Change due: $", payment-total_price, "\nThank you, enjoy your coffee!")