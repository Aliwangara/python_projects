



expense_file = "expenses.txt"

while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")

    choice = int(input("Enter a number from the options above:  "))

    if choice == 1:
        try:
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            item = input("Enter item name:  ").lower().strip()
            amount = float(input("enter amount: "))

            with open(expense_file,'a',newline="") as f:
                f.write(f"Date: {date} | Item: {item} | Amount: {amount:.2f}\n")

        except ValueError:
            print("please Enter correct amount")
        
    elif choice ==2:
        try:
            with open(expense_file,'r') as f:
                print("===📘 Your Expenses===")
                data = f.read()

                if data.strip() == "":
                    print("No records available")
                else:
                    print(data)
        except FileNotFoundError:
            print("⚠️ Expense file not found.")

    elif choice == 3:
        print("Thank you for using the expense tracker")
        break
    else:
        print("❌ Invalid choice.")


