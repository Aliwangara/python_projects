from currency_class import Currency as c
import requests as r


currency_api_key =  "ec255ab3e019e552750c39e7"

url = f'https://v6.exchangerate-api.com/v6/{currency_api_key}/latest/USD'

response = r.get(url)
data = response.json()
new_data = data.get('conversion_rates')



def main():
    currency()


def currency():
    amount = float(input("Enter Amount:  "))
    source_currency = input("Enter The currency you have now eg(USD, KSH): ").upper()
    target_currency  = input("Which currency are you changing to: ").upper()

    if source_currency not in new_data and target_currency not in new_data:
           print("Invalid Currency")
           return
    amount_in_usd = amount /new_data[source_currency]
    converted_currency = amount_in_usd * new_data[target_currency]
    
    print(f"{converted_currency}")

def save_converted_currency():
     
    


if __name__ =="__main__":
    main()

