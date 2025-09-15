

class Expense:
    def __init__(self, name,category, amount):
        self.name= name
        self.category = category
        self.amount = amount
    def __repr__(self):
        return f"name: {self.name}.\nCategory: {self.category}. \nAmount: {self.amount}"