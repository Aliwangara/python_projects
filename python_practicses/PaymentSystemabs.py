# Abstract Base Class: PaymentMethod

# Private Attribute:

# __amount

# Methods:

# __init__(self, amount)

# get_amount() → returns the amount

# payment_info() → prints "Payment Amount: $<amount>"

# @abstractmethod process_payment() → must be implemented by subclasses

# 💳 Subclass: CreditCardPayment

# Private Attributes:

# __card_number

# Methods:

# __init__(self, amount, card_number)

# process_payment() → prints
# "Processing Credit Card payment of $<amount> using card ending with XXXX"

# 💻 Subclass: PayPalPayment

# Private Attributes:

# __email

# Methods:

# __init__(self, amount, email)

# process_payment() → prints
# "Processing PayPal payment of $<amount> for account <email>"

# 💸 Subclass: BankTransferPayment

# Private Attributes:

# __bank_name

# __account_number

# Methods:

# __init__(self, amount, bank_name, account_number)

# process_payment() → prints
# "Processing Bank Transfer of $<amount> from <bank_name> account ending with XXXX"

# Program Flow

# Create three objects:

# credit = CreditCardPayment(1200, "1234567890123456")
# paypal = PayPalPayment(800, "user@example.com")
# bank = BankTransferPayment(2500, "Equity Bank", "9876543210")


# Store them in a list.

# Loop through each payment:

# Show payment info.

# Process the payment.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self,amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount
    def payment_info(self):
        print(f"Payment Amount: {self.get_amount()}")
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, amount,card_number):
        super().__init__(amount)
        self.__card_number = card_number
    def get_card_number(self):
        return self.__card_number
    def process_payment(self):
        super().process_payment()
        print(f"Processing Credit Card payment of ${self.get_amount()} using card ending with {self.get_card_number()[-4:]}")

class PayPalPayment(PaymentMethod):
    def __init__(self, amount,email):
        super().__init__(amount)
        self.__email = email
    def get_email(self):
        return self.__email
    def process_payment(self):
        super().process_payment()
        print(f"Processing PayPal payment of ${self.get_amount()} for account: {self.get_email()}")

class BankTransferPayment(PaymentMethod):
    def __init__(self, amount,bank_name,account_number):
        super().__init__(amount)
        self.__bank_name = bank_name
        self.__account_number = account_number
    def get_bank_name(self):
        return self.__bank_name
    def get_account_number(self):
        return self.__account_number
    def process_payment(self):
        super().process_payment()
        print(f"Processing Bank Transfer of ${self.get_amount()} from {self.get_bank_name()} account ending with {self.get_account_number()[-4:]}")

        
credit = CreditCardPayment(1200, "1234567890123456")
paypal = PayPalPayment(800, "user@example.com")
bank = BankTransferPayment(2500, "Equity Bank", "9876543210")

info_storage = [credit,paypal,bank]

for info in info_storage:
    info.payment_info()
    info.process_payment()
    print("-" * 50)






