# Mini Inventory System

# You’ll build a CLI program to manage a small shop’s inventory.

# Features:

# Add item

# Ask for item name, quantity, and price.

# Store as a dictionary:

# {"name": "Apple", "quantity": 20, "price": 10.5}


# View all items

# List all items with their total value (quantity * price).

# Search item

# Ask for name → show details if found.

# Most valuable item

# Use max(..., key=lambda ...) to find the item with the highest total value.

# Sort items

# Option to sort by name or total value.

# Update stock

# Increase or decrease quantity for an existing item.

# Exit

# 🔑 Concepts Used:

# Variables, Lists, Dictionaries

# Functions

# Loops (for + while)

# If/Else

# Lambda (max and sorted)

# Arithmetic operations

# 💡 Hint: Use a list of dictionaries, just like your students project.

# For “most valuable item”: max(items, key=lambda x: x['quantity']*x['price'])

# For sorting by total value: sorted(items, key=lambda x: x['quantity']*x['price'], reverse=True)


item_list = []


def add_item():
    item_name = input("Enter name of the item:    ").lower()
    item_quantity = int(input("Enter Item quantity:   "))
    price = float(input("Enter price of the item:   "))

    item_info = {
        "name": item_name,
        "quantity": item_quantity,
        "price": price
    }
    item_list.append(item_info)


def view_items():
    for item in item_list:
        
        print(f"You picked {item['name']}\nQuantity: {item["quantity"]} Price per item is "
              f"{item['price']}\nTotal is: {item['quantity'] * item['price']:.2f}")
view_items()

def search_item():
    search_input = input(
        "Enter name of the item you are looking for:   ").lower()
    for item in item_list:
        if search_input in item["name"]:
            print(f"{search_input} is available. Costing {item['price']} each")
        else:
            print(f"{search_input} Isn't available")


def most_valuable_item():
    valuable_item = max(item_list, key=lambda i: i['price'] * i['quantity'])
    print(f"Most valuable Item is: {valuable_item}")


def sorting_items():

    sorting = sorted(item_list, key=lambda s: (
        s['name'], s['quantity'] * s['price']))
    print(f"Sorted items: {sorting}")


def increase_decrease():
    print("==== Items Available ====")
    for i, list_number in enumerate(item_list, 1):
        print(f"{i}. {list_number}")
    list_item_input = int(
        input("Select  the number of item you want to increase it's quantity:  ")) - 1

    if 0 <= list_item_input <= len(item_list):
        inc_dec = input("Which operation do you want to perform (- or +):   ")
        number_input = int(
            input("Enter quantity you want to increase or decrease:  "))

        if inc_dec == "+":
            item_list[list_item_input]["quantity"] += number_input
        elif inc_dec == "-":
            item_list[list_item_input]["quantity"] -= number_input
        else:
            print("Invalid operation")

        print(
            f"Updated: {item_list[list_item_input]['name']} now has quantity {item_list[list_item_input]['quantity']}")
    else:
        print("Invalid selection!")


while True:
    print("1. add item")
    print("2. view items")
    print("3. search item")
    print("4. most valuable item ")
    print("5. sorting items ")
    print("6. increase decrease")
    print("7. Exit")

    option_input = int(input("Select the number of input you want to use:  "))

    if option_input == 1:
        add_item()
    elif option_input == 2:
        view_items()
    elif option_input == 3:
        search_item()
    elif option_input == 4:
        most_valuable_item()
    elif option_input == 5:
        sorting_items()
    elif option_input == 6:
        increase_decrease()
    elif option_input == 7:
        print("== These are the items available ==")
        print(f"{item_list}")
        break
    else:
        print("Please select the available numbers")
