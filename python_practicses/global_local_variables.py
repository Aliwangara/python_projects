# # A global variable balance = 1000.

# # A function deposit(amount) that adds to balance.

# # A function withdraw(amount) that subtracts from balance.

# # Print balance after each operation.

# balance = 1000

# def deposit(amount):
#     global balance
#     balance +=amount
#     print(f"deposited Amount is: {amount}. Balance is {balance}")

# deposit(500)

# def withdraw(amount):
#     global balance
#     if amount <= balance:
#      balance -= amount
#      print(f"Withdrew {amount}. balance {balance}")
#     else:
#        print("Insufficient funds")
#     #    
# withdraw(200)


balance = 20000

def deposit(amount):
    global balance

    balance += amount
    print(f"You have deposited {amount}. Your balance is {balance}")


def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print(f"You have withdrawn: {amount}. your balance is: {balance}")
    else:
        print(f"Can't withdraw {amount} you have insufficient funds")


def check_balance():
    print(f"Your balance is {balance}")




print("------- Welcome to Alis Bank --------")

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice  = input("Enter a number from the choices above:  ")

    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        deposit(amt)
    elif choice =="2":
        amt = float(input("Enter deposit amount: "))
        withdraw(amt)
    elif choice == "3":
        check_balance()
    elif choice =="4":
        print("Bye. Wish to see you soon")
        break
    else:
        print("please select an option")
        








