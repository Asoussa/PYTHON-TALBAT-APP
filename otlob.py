from datetime import datetime
import random


print("Hello my friend, please register to proceed: ")
name = input("Enter your name: ")
phone = int(input("Enter your phone number (digits only): "))
address = input("Enter your address: ")
username = input("Enter your username: ")
password = input("Enter your password: ")

print("\nRegistration Complete!")
print(f"Name: {name} ", end="")
print(f"Phone: {phone} ", end="")
print(f"Address: {address} ", end="")
print(f"Username: {username} ", end="")
print(f"Password: {password} ", end="")
print("\nHello! Welcome to Talabat\n")


def display_categories():
    print("Choose a category:")
    print("1 - FOOD")
    print("2 - GROCERIES")
    print("3 - HEALTH AND BEAUTY")


def display_restaurants_food():
    print("Choose a restaurant:")
    print("1 - BAZOOKA")
    print("2 - PIZZA KING")
    print("3 - HEART ATTACK")


def display_restaurants_groceries():
    print("Choose a store:")
    print("1 - CARREFOUR")
    print("2 - BIM")
    print("3 - HEALTHY")


def display_restaurants_health_and_beauty():
    print("Choose a pharmacy:")
    print("1 - LIFE PHARMACY")
    print("2 - AL Sydly PHARMACY")
    print("3 - HELAL PHARMACY")
    
    
def menu_bazooka():
    print("BAZOOKA MENU:")
    print("1 - Chicken Wrap\tPRICE: 50")
    print("2 - Beef Burger\tPRICE: 70")
    print("3 - Family Meal\tPRICE: 120")


def menu_pizza_king():
    print("PIZZA KING MENU:")
    print("1 - Margherita Pizza\tPRICE: 80")
    print("2 - Pepperoni Pizza\tPRICE: 100")
    print("3 - Veggie Pizza\tPRICE: 90")


def menu_heart_attack():
    print("HEART ATTACK MENU:")
    print("1 - Cheese Explosion Burger\tPRICE: 90")
    print("2 - Ultimate Fries\tPRICE: 60")
    print("3 - Double Trouble Burger\tPRICE: 110")



def menu_carrefour():
    print("CARREFOUR MENU:")
    print("1 - Rice (5kg) \t PRICE: 150")
    print("2 - Olive Oil (1L)\tPRICE: 200")
    print("3 - Bread (1 pack)\tPRICE: 20")


def menu_bim():
    print("BIM MENU:")
    print("1 - Milk (1L)\tPRICE: 50")
    print("2 - Eggs (12 pcs)\tPRICE: 30")
    print("3 - Butter (200g)\tPRICE: 70")


def menu_healthy():
    print("HEALTHY MENU:")
    print("1 - Organic Almonds\tPRICE: 300")
    print("2 - Fresh Salad\tPRICE: 100")
    print("3 - Smoothie Pack\tPRICE: 150")


def menu_life_pharmacy():
    print("LIFE PHARMACY MENU:")
    print("1 - Limitless Man\tPRICE: 190")
    print("2 - Milga Advance\tPRICE: 230")
    print("3 - Synjardy\tPRICE: 450")


def menu_al_sydly_pharmacy():
    print("AL SAYED PHARMACY MENU:")
    print("1 - Trental SR 400 MG\tPRICE: 80")
    print("2 - Dermatol Gauze\tPRICE: 30")
    print("3 - Abimol 300 GM\tPRICE: 40")


def menu_helal_pharmacy():
    print("HELAL PHARMACY MENU:")
    print("1 - EVA Face Wash\tPRICE: 300")
    print("2 - Meloquin\tPRICE: 400")
    print("3 - L'Oreal Excellence\tPRICE: 350")
    
def add_to_cart():
    cart = []  
    total_price = 0  

    while True:
        display_categories()
        category = input("\nEnter your choice (1-3) or 'q' to quit shopping: ")

        if category == "1":  
            display_restaurants_food()
            restaurant = input("\nEnter your choice (1-3) or 'b' to go back: ")

            if restaurant == "1":  
                menu_bazooka()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "Chicken Wrap"
                    price = 50
                elif item == "2":
                    item_name = "Beef Burger"
                    price = 70
                elif item == "3":
                    item_name = "Family Meal"
                    price = 120
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue

            elif restaurant == "2":  
                menu_pizza_king()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "Margherita Pizza"
                    price = 80
                elif item == "2":
                    item_name = "Pepperoni Pizza"
                    price = 100
                elif item == "3":
                    item_name = "Veggie Pizza"
                    price = 90
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue

            elif restaurant == "3": 
                menu_heart_attack()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "Cheese Explosion Burger"
                    price = 90
                elif item == "2":
                    item_name = "Ultimate Fries"
                    price = 60
                elif item == "3":
                    item_name = "Double Trouble Burger"
                    price = 110
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue

            else:
                print("Invalid restaurant choice.")
                continue

        elif category == "2":  
            display_restaurants_groceries()
            restaurant = input("\nEnter your choice (1-3) or 'b' to go back: ")
            if restaurant == "1":  
                menu_carrefour()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "Rice"
                    price = 150
                elif item == "2":
                    item_name = "Olive Oil"
                    price = 200
                elif item == "3":
                    item_name = " Bread"
                    price = 20
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue
                
                
            elif restaurant == "2":  
                menu_bim()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "Milk "
                    price = 50
                elif item == "2":
                    item_name = " Eggs"
                    price = 30
                elif item == "3":
                    item_name = "Butter"
                    price = 70
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue
                
                        
            elif restaurant == "3":  
                menu_healthy()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "Organic Almonds"
                    price = 300
                elif item == "2":
                    item_name = "Fresh Salad"
                    price = 100
                elif item == "3":
                    item_name = "Smoothie Pack"
                    price = 150
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue




        elif category == "3": 
            display_restaurants_health_and_beauty()
            restaurant = input("\nEnter your choice (1-3) or 'b' to go back: ")

            if restaurant == "1": 
              menu_life_pharmacy()
        
              item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

              if item == "1":
                    item_name = " Limitless Man"
                    price = 190
              elif item == "2":
                    item_name = "Milga Advance"
                    price = 230
              elif item == "3":
                    item_name = "Synjardy"
                    price = 450
              elif item == "b":
                    continue
              else:
                    print("Invalid choice.")
                    continue
                
              
            elif restaurant == "2":  
                menu_al_sydly_pharmacy()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = " Trental SR 400 MG"
                    price = 80
                elif item == "2":
                    item_name = "Dermatol Gauze"
                    price = 30
                elif item == "3":
                    item_name = "Abimol 300 GM"
                    price = 40
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue
                
  
  
            elif restaurant == "3":  
                menu_helal_pharmacy()
                item = input("\nEnter the menu item number to add to cart (or 'b' to go back): ")

                if item == "1":
                    item_name = "EVA Face Wash"
                    price = 300
                elif item == "2":
                    item_name = "Meloquin"
                    price = 400
                elif item == "3":
                    item_name = "Abimol 300 GM"
                    price = 350
                elif item == "b":
                    continue
                else:
                    print("Invalid choice.")
                    continue

                
                
                
                

        elif category == "q":  
            print("\n Thank you for shopping! Proceeding to checkout...")
            break

        else:
            print("Invalid category choice. Please try again.")
            continue

        
        quantity = int(input(f"How many {item_name} would you like to add? "))
        cart.append((item_name, quantity, price))
        total_price += quantity * price
        print(f"\nAdded {quantity} quantity from {item_name} to cart. Current total: {total_price}.\n")

    
        continue_shopping = input("Do you want to countinue shopping ? (yes/no): ").strip().lower()
        if continue_shopping != 'yes':
            break

    print("\nFinal Cart Summary:")
    for item_name, quantity, price in cart:
        print(f"- {item_name}: {quantity} pices and {price} price each = {quantity * price}")
    print(f"Total Price: {total_price}\n")

    return cart, total_price



def checkout(name, phone, address, cart, total_price):
    print("\n--- Checkout ---")
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")
    print("\nYour Cart:")
    for item_name, quantity, price in cart:
        print(f"- {item_name}: {quantity} pices and price {price} each")



    print("\nChoose a payment method:")
    print("1 - Visa")
    print("2 - Cash")
    payment_choice = input("Enter your choice (1 or 2): ")

    if payment_choice == "1":
        print("You have chosen Visa. Proceeding with payment...")
        payment_method = "Visa"
    elif payment_choice == "2":
        print("You have chosen Cash. Proceeding with payment...")
        payment_method = "Cash"
    else:
        print("Invalid choice. Please try again.")
        return checkout(name, phone, address, cart, total_price) 

    print("\nOrder successfully placed!")
    print("Thank you for shopping with Talabat!")
    return payment_method


def display_order_details(name, phone, address, cart, total_price, payment_method):
    print(f"Mr. {name}")

    now = datetime.now()
    print("Date of the order is:", now)

    order_number = random.randint(1, 1000)
    print("Your order number is:", order_number)

    print("You want to receive your order at:", address)
    print("Your phone is:", phone)

    print("\nOrder Items:")
    for item_name, quantity, price in cart:
        print(f"{quantity} x {item_name} with price {price} each")

    service_fee = 0.14
    delivery_fee = 45
    amount = total_price * (1 + service_fee) + delivery_fee
    service_feee=int(service_fee* 100)
    print(f"Service Fee: {service_feee }")
    print(f"Delivery Fee: {delivery_fee}")
    print(f"Total Amount: {amount}")

    print(f"Payment Method: {payment_method}")
    print("\nThank you for your order! Your order will be delivered soon.")


cart, total_price = add_to_cart()
if total_price > 0:
    payment_method = checkout(name, phone, address, cart, total_price)
    display_order_details(name, phone, address, cart, total_price, payment_method)
else:
    print("No items in cart. Exiting program.")