cart = {}
total_amount = 0

print("---------Welcome to Nuel Supermarket!------------")

while True:
    print('Press 1 to Add an item')#\nPress 2 to view the menu\nPress 3 to remove an item\nPress 4  to make payment\npress 5 to exit')
    #print('Press 2 to Add an item')
    #print('Press 3 to remove an item')
    #print('Press 4  to make payment')
    #print('press 5 to exit')

    choice = input("Enter a number (1-5):").strip()
    
    if choice == "1":
        # get product details
        item = input('Enter product name:').strip()
        qty = int(input("Enter quantity:").strip())
        
        if item in cart:
            print("yes")
            print(f"quantity, price in the cart:{cart[item]}")
            
            amt, quantity = cart[item] # from  the cart, get the total price and the quantity
            unit_price = amt / quantity # divide total amt by the quantity in the cart
            print(f"Unit price:{unit_price}")
            new_qty = qty + quantity  # add new quantiy + old quantity
            new_amt = unit_price * new_qty # multiply total quantity by unit price

            cart[item] = [new_amt, new_qty] # save the amount  and quantity
            print(f"new quantity, price of the product: {cart[item]}")




          

      
        else:
            price = float(input("enter price"))
            amt = price * qty

            cart[item]= [amt, qty]
            print("item added")

    




        
    elif choice == "2":
        for x in cart:
            print(x)

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    else:
        print("Incorrect option")
        break
    
for name, value in cart.items():
    
    amount = value[0]
    total_amount += amount



print(total_amount)

