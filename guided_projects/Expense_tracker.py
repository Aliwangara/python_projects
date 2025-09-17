from typing import List
from expense import Expense
import calendar
import datetime


def main():
    budget  = 2000 

    expense_file_path = "expenses.csv"

    expense = get_user_expense()
    

    save_user_expense(expense, expense_file_path)

    summarize_expense(expense_file_path, budget)





def get_user_expense():
        expense_name = input("Enter name of your expense: ").capitalize()
        expense_amount = float(input("Enter Expense Amount: "))
        print(f"You have entered {expense_name}, {expense_amount}")

        expense_categories= ["Food","Home", "Work", "Misc"]

        while True:
              for i , categories_name in enumerate(expense_categories,1):
                    print(f" {i}. {categories_name}")
              value_range = f"[1- {len(expense_categories)}]"
             
              selected_index = int(input(f"enter a category number {value_range}: ")) -1
              
             

              if selected_index in range(len(expense_categories)):
                    new_category = expense_categories[selected_index]
                    new_expense =Expense(
                          name=expense_name, category=new_category, amount=expense_amount
                                         )
                    return new_expense
                    
              else:
                    print("invalid Category. Please Try again")
                    
              




def save_user_expense(expense:Expense ,expense_file_path):
        print(f"saving user expense: {expense} to {expense_file_path}")
        with open(expense_file_path, "a") as f:
              f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")
              



def summarize_expense(expense_file_path,budget):
        expenses : List[Expense]= []
        with open(expense_file_path, "r") as f:
              for line in f:
                    name, amount, category = line.strip().split(",")
                    print(name, amount, category)
                    expenses.append(Expense(name=name, amount=float(amount), category=category))
        amount_by_category = {}
        for expense in expenses:
              key = expense.category
              if key in amount_by_category:
                    amount_by_category[key] += expense.amount
              else:
                    amount_by_category[key]  = expense.amount
        print("Expenses by Category")
        for key, amount in amount_by_category.items():
              print(f" {key} : $ {amount:.2f}")

        total_spent = sum([ex.amount for ex in expenses])
        print(f"You've spent ${total_spent:.2f} this month!")

        remaining_budget = budget - total_spent
        print(f"budget Remaining ${remaining_budget:.2f} this month!")

        now = datetime.datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        remaining_days = days_in_month - now.day

        daily_budget = remaining_budget / remaining_days
        print(f"budget per day: ${daily_budget:.2f}")
        



if __name__ == "__main__":
    main()