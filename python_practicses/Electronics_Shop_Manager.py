# You have this list:

electronics = [
    {"name": "phone", "quantity": 15, "price": 300},
    {"name": "laptop", "quantity": 7, "price": 1000},
    {"name": "headphones", "quantity": 20, "price": 50},
    {"name": "charger", "quantity": 12, "price": 20}
]

# Your Task:

# Print all items in menu form with indexes:

# 1. phone → 15pcs @ $300
# 2. laptop → 7pcs @ $1000
# 3. headphones → 20pcs @ $50
# 4. charger → 12pcs @ $20


# Ask user to select an item by number.

# Give them two options:

# Update quantity (+ or -)

# Update price

# If they choose quantity, ask how much to add/remove and update.

# If they choose price, ask for the new price and update.

# Print only the updated item with new details.


for i ,electronics_index in enumerate(electronics,1):
    print(f"{i}. {electronics_index}")

item_number_input = int(input("Enter the number of input you want to select:   "))-1


if 0<= item_number_input < len(electronics):
    price_quantity_selection = input("Choose what you want to update(p for price or q for quantity):  ").lower()

    if price_quantity_selection == 'q' or price_quantity_selection =='quantity':
        operation = input("Enter operation you need to perform(+ or -):  ")
        quantity_input = int(input("How many Items do you want to add or remove:   "))
        
        if operation == '+':
            electronics[item_number_input]['quantity'] += quantity_input
        elif operation == '-':
            electronics[item_number_input]['quantity'] -= quantity_input
        else:
            print(f"{operation} is invalid please enter a valid operation")
        print(f"Updated: {electronics[item_number_input]["name"]}  {electronics[item_number_input]['quantity']}")
    elif price_quantity_selection == 'p' or price_quantity_selection =='price':
        operation = input("Enter operation you need to perform(+ or -):  ")
        price_input = float(input("How much do you want to add or remove:   "))
        

        if operation == '+':
            electronics[item_number_input]['price'] += price_input
        elif operation == '-':
            electronics[item_number_input]['price'] -= price_input
        else:
            print(f"{operation} is invalid please enter a valid operation")
        print(f"Updated: {electronics[item_number_input]["name"]} quantity to {electronics[item_number_input]['price']}")
    else:
        print("select either a price or quantity option")
