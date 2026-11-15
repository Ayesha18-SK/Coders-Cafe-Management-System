menu = {
    'pizza' : 100,
    'salad' : 50,
    'burger' : 130,
    'pop corn' : 150,
    'chicken puff' : 80,
}

print("Welcome to our Coders Cafe")

print('Pizza: 100\nSalad : 50\nBurger : 130\nPop Corn : 150\nChicken Puff : 80')

order_total = 0 

ordered_items = []

while True:
    order_item = input("Enter your item:").lower().strip()
    
    if order_item in menu:
        order_total += menu[order_item]
        ordered_items.append(order_item)
        
        print(order_item, 'added to your order!')
        
    else:
        print("You entered a wrong item")
        
    order = input("Do you want anything else?(yes/no):").lower().strip()
    
    if order  != "yes":
       break

print("\nYour order")

for item in ordered_items:
    print(item, ":", menu[item])
    
print('Your order value:', order_total)
print("Thank you for visiting Coders Cafe!")
        

