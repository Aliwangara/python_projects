from currency_class import Currency 
import requests as r


currency_api_key =  "ec255ab3e019e552750c39e7"



url = f'https://v6.exchangerate-api.com/v6/{currency_api_key}/latest/USD'

response = r.get(url)
data = response.json()
new_data = data.get('conversion_rates')



def main():
    currency_history = "solo_projects/currency_converter/currency.csv"
    currency_function = currency()
    save_converted_currency(currency_function, currency_history)


def currency():
    amount = float(input("Enter Amount:  "))
    source_currency = input("Enter The currency you have now eg(USD, KSH): ").upper()
    target_currency  = input("Which currency are you changing to: ").upper()

    if source_currency not in new_data and target_currency not in new_data:
           print("Invalid Currency")
           return
    amount_in_usd = amount /new_data[source_currency]
    converted_currency = amount_in_usd * new_data[target_currency]

    new_currency_data = Currency(amount=amount,from_currency= source_currency, to_currency=target_currency, converted_currency=converted_currency)

    return new_currency_data
    
    

def save_converted_currency(currency_function:Currency, currency_history):
        print(f"saving {currency_function} to {currency_history[-12:]}")
        with open(currency_history , "a") as f:
            
            f.write(f"From  {currency_function.from_currency}: {currency_function.amount} to {currency_function.to_currency}: {currency_function.converted_currency} \n")

              
          
     
    


if __name__ =="__main__":
    main()

