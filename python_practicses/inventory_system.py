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