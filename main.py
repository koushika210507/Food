from login import login
from menu import display_menu
from cart import add_to_cart, view_cart
from order_tracking import track_order
from profile import profile
from reservation import reserve_table

print("===== WELCOME TO FOOD  EXPRESS =====")
print("hi welcome to food express!")
role = login()

if role == "Customer":

    while True:

        print("\n1. View Menu")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Track Order")
        print("5. Profile")
        print("6. Reserve Table")
        print("7. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            display_menu()
            add_to_cart()

        elif choice == "3":
            view_cart()

        elif choice == "4":
            track_order()

        elif choice == "5":
            profile()

        elif choice == "6":
            reserve_table()

        elif choice == "7":
            print("Thank You")
            break

        else:
            print("Invalid Choice")