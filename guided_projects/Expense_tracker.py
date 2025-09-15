from expense import Expense


def main():

    expense_file_path = "expenses.csv"

    expense = get_user_expense()
    

    save_user_expense(expense, expense_file_path)

    summarize_expense(expense_file_path)





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
              



def summarize_expense(expense_file_path):
        expenses = []
        with open(expense_file_path, "r") as f:
             new_lines =  f.readlines()
             for line in new_lines():
                   print(line)
        #            expense_name,expense_amount,expense_category = line.sptrip().split(",")
        #            line_expense =Expense(name = expense_name, amount=float(expense_amount), category=expense_category)
        #            print(line_expense)
        #            expenses.append(line_expense)
        # print(expenses)



if __name__ == "__main__":
    main()