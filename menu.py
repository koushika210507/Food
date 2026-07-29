food_menu = {
    1: ("Pizza", 250),
    2: ("Burger", 150),
    3: ("Pasta", 200),
    4: ("French Fries", 120),
    5: ("Coke", 50)
}

def display_menu():

    print("\n===== FOOD MENU =====")

    for item_id, item in food_menu.items():
        print(item_id, "-", item[0], "- ₹", item[1])