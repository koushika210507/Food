def login():

    print("\n===== FoodExpress Login =====")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    print("\nSelect Role")
    print("1. Customer")
    print("2. Restaurant Owner")

    choice = input("Enter Choice : ")

    if choice == "1":
        role = "Customer"

    elif choice == "2":
        role = "Restaurant Owner"

    else:
        print("Invalid Role")
        return None

    print("\nLogin Successful")
    print("Welcome", username)

    return role