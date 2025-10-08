# Requirements
# Class: Product

# Private Attributes:

# __name

# __price

# __stock

# Class Attribute:

# __store_name = "TechMart"

# Methods:

# __init__(self, name, price, stock) → initialize product details

# product_info(self) → prints

# Product: <name>, Price: $<price>, Stock: <stock>, Store: <store_name>


# @classmethod change_store(cls, new_store)

# changes the store name for all products

# @staticmethod is_valid_price(price)

# returns True if price > 0, else False

# 🧮 Program Flow

# Create three products:

# p1 = Product("Laptop", 1200, 10)
# p2 = Product("Headphones", 150, 25)
# p3 = Product("Mouse", 40, 50)


# Check if a given price is valid using Product.is_valid_price(-100).

# Display all product info.

# Change the store name using Product.change_store("ElectroHub").

# Display all product info again to confirm the change.


class Product:
    __store_name = "TechMart"
    def get_store_name(self):
        return self.__store_name
    def __init__(self,name,price,stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_name(self):
            return self.__name
    def get_price(self):
            return self.__price
    def get_stock(self):
            return self.__stock
    def product_info(self):
          print(f"Product: {self.get_name()}, Price: ${self.get_price()}, Stock: {self.get_stock()}, Store: {self.get_store_name()}")
    @classmethod
    def change_store(cls,new_store):
            cls.store_name = new_store
    @staticmethod
    def is_valid_price(price):
            return price >0
              

p1 = Product("Laptop", 1200, 10)
p2 = Product("Headphones", 150, 25)
p3 = Product("Mouse", 40, 50)

print("Is -100 a valid price?", Product.is_valid_price(-100))
print()

# Display all product info
for p in [p1, p2, p3]:
    p.product_info()

# Change store name

Product.change_store("ElectroHub")

print("\n--- After Store Change ---\n")
for p in [p1, p2, p3]:
    p.product_info()

    p.product_info()

