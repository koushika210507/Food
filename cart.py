from menu import food_menu

cart = []

def add_to_cart():

    item = int(input("Enter Item Number : "))

    if item in food_menu:
        cart.append(food_menu[item])
        print(food_menu[item][0], "added to cart")

    else:
        print("Invalid Item")

def view_cart():

    if len(cart) == 0:
        print("Cart is Empty")
        return

    total = 0

    print("\n===== YOUR CART =====")

    for item in cart:
        print(item[0], "- ₹", item[1])
        total += item[1]

    print("Total Bill : ₹", total)