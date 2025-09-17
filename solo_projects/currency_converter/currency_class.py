

class Currency:
    def __init__(self, amount,from_currency,to_currency, converted_currency):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.converted_currency = converted_currency
    def __repr__(self):
       return f"{self.amount} \n {self.from_currency} \n {self.to_currency} \n {self.converted_currency}"