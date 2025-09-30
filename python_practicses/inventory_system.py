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


item_list= []
def add_item():
    item_name = input("Enter name of the item:    ").lower()
    item_quantity = int(input("Enter Item quantity:   "))
    price = float(input("Enter price of the item:   "))

    item_info = {
        "name":item_name,
        "quantity":item_quantity,
        "price":price
    }
    item_list.append(item_info)

add_item()

def view_items():
    for item in item_list:
        print(f"You picked {item['name']}\nQuantity: {item["quantity"]} Price per item is "
               f"{item['price']}\nTotal is: {item['quantity'] * item['price'] :.2f}") 

view_items()

def search_item():
    search_input = input("Enter name of the item you are looking for:   ").lower()
    for item in item_list:
        if search_input in item["name"]:
            print(f"{search_input} is available. Costing {item['price']} each")
        else:
            print(f"{search_input} Isn't available")

search_item()

def most_valuable_item():
    valuable_item = max(item_list, key=lambda i:i['price'] * i['quantity'])
    print(f"Most valuable Item is: {valuable_item}")
    

most_valuable_item()

def sorting_items():

  sorting = sorted(item_list, key=lambda s:(s['name'], s['quantity'] * s['price']))
  print(f"Sorted items: {sorting}")

sorting_items()

def increase_decrease():
    for new_item in item_list:
        if new_item in item_list:
              
        



increase_decrease()