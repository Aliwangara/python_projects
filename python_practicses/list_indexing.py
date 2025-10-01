# Now, let’s turn it into a mini exercise for you

# Here’s a list:

fruits = [
    {"name": "apple", "quantity": 10, "price": 2},
    {"name": "banana", "quantity": 5, "price": 1},
    {"name": "orange", "quantity": 8, "price": 1.5}
]


#  Your task:

# Print the name of the second fruit.

# Print the price of the last fruit.

# Increase the quantity of the first fruit by 5.

# Decrease the quantity of the orange by 3.

# Print the updated list.

# second_fruit = fruits[1]['name']
# last_fruit = fruits[2]['price']
# quantity_first = fruits[0]['quantity']+5
# quantity_orange = fruits[2]['quantity']+1.5

# print(quantity_orange)


# Exercise: Grocery Stock Manager

# You have this list of groceries:

groceries = [
    {"name": "rice", "quantity": 10, "price": 50},
    {"name": "sugar", "quantity": 5, "price": 100},
    {"name": "flour", "quantity": 8, "price": 70},
    {"name": "oil", "quantity": 3, "price": 200}
]

# Your Task:

# Print all groceries in a menu format, like:

# 1. rice → 10kg @ 50
# 2. sugar → 5kg @ 100
# 3. flour → 8kg @ 70
# 4. oil → 3L @ 200


# Ask the user to select an item by number (use index with [ ]).

# Ask how much quantity to add to that item.

# Update the list with the new quantity.

# Print the updated item only (not the whole list).



for i, groceries_index in enumerate(groceries, 1):
    print(f"{i}. {groceries_index['name']} -> {groceries_index['quantity']}kg @ {groceries_index['price']}")

item_by_number = int(input("Enter number of the item you want to select:   "))-1

if 0<= item_by_number < len(groceries):
    operation = input("Enter operation you want to perform(+ or -): ")
    item_quantity = int(input("Enter the number of quantities you want to add or remove:   "))

    if operation =="+":
        groceries[item_by_number]['quantity'] += item_quantity
    elif operation == "-":
        groceries[item_by_number]['quantity'] -= item_quantity
    else:
        print("please enter a valid operation")
    print(f"Update {groceries[item_by_number]['name']} now has quantity {groceries[item_by_number]['quantity']}Kg")
else:
    print("Invalid Selection")
     

