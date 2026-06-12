#ASSIGNMENT2

"""
Create an E-Commerce that checks inputs like subtotal, discount and tax to calculate the 
final price of a product .
include the coupon code for discount and tax rate for the calculation.
use nested conditions to handle different scenarios such as  valid/invalid coupon code, 
and different tax rates based on the location, and various discount levels based on
the subtotal amount.
implement login system for the e-commerce platform that checks user credentials in the system.
there are three types of users: admin, customers and cashiers.
Each user has a password and different access levels.
Admin can access all features, customers can only view products and make purchases.
"""

# File-based user storage

users = {}

try:
    file = open("users.txt", "r")
    for line in file:
        username, password, role = line.strip().split(",")
        users[username] = (password, role)
    file.close()
except:
    print("users.txt not found, creating new file...")
    open("users.txt", "w").close()


# MAIN LOOP
while True:
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose option: ")

    # REGISTER
    if choice == "2":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        role = input("Enter role (Admin/Customer/Cashier): ")

        file = open("users.txt", "a")
        file.write(f"{username},{password},{role}\n")
        file.close()

        print("User registered successfully!")

        # Reload users
        users = {}
        file = open("users.txt", "r")
        for line in file:
            u, p, r = line.strip().split(",")
            users[u] = (p, r)
        file.close()

    # LOGIN
    elif choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            if users[username][0] == password:
                role = users[username][1]
                print("Login successful!")
                print(f"Welcome {role}!")

                # PROCESS ORDER (for all roles)
                subtotal = float(input("Enter subtotal: "))

                # Subtotal discount
                if subtotal > 1000:
                    base_discount = 0.15
                elif subtotal > 500:
                    base_discount = 0.10
                else:
                    base_discount = 0.05

                # Coupon
                coupon = input("Enter coupon code: ")

                if coupon == "SAVE10":
                    coupon_discount = 0.10
                elif coupon == "SAVE20":
                    coupon_discount = 0.20
                else:
                    coupon_discount = 0

         # Nested condition
                if coupon_discount > 0:
                    print("Valid coupon applied!")
                else:
                    print("Invalid coupon.")

                total_discount = base_discount + coupon_discount
                discounted_price = subtotal - (subtotal * total_discount)

                # Tax by location
                location = input("Enter location (Kampala/Wakiso/Other): ")

                if location.lower() == "kampala":
                    tax_rate = 0.18
                elif location.lower() == "wakiso":
                    tax_rate = 0.15
                else:
                    tax_rate = 0.10

                tax = discounted_price * tax_rate
                final_price = discounted_price + tax

                # Output
                print("\n----- RECEIPT -----")
                print(f"Subtotal: {subtotal}")
                print(f"Discount: {total_discount * 100}%")
                print(f"After Discount: {discounted_price}")
                print(f"Tax: {tax}")
                print(f"Final Price: {final_price}")
                print("-------------------")

            else:
                print("Wrong password.")
        else:
            print("User not found.")

    # EXIT
    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid option.")