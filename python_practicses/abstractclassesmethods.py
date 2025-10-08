from abc import ABC,abstractmethod

class Payment(ABC):
    def __init__(self,amount):
        self.__amount = amount
    def get_amount(self):
            return self.__amount
        

    @abstractmethod
    def process_payment(self):
        pass
    def payment_info(self):
        print(f"Payment Amount: {self.__amount}")

class PaypalPayment(Payment):
        def __init__(self, amount,email):
          super().__init__(amount)
          self.__email = email
        def process_payment(self):
            print(f"Processing PayPal payment of ${self.get_amount()} for {self.__email}")

class CreditCard(Payment):
        def __init__(self, amount,card_number):
          super().__init__(amount)
          self.__card_number = card_number
        def process_payment(self):
          print(f"Processing Credit Card payment of ${self.get_amount()} using card {self.__card_number[-4:]}")
        
payments = [
    PaypalPayment(100, "user@example.com"),
    CreditCard(250, "1234567812345678")
]

for p in payments:
     p.payment_info()
     p.process_payment()
    
