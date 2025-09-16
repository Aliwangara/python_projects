from currency_class import Currency as c
import requests as r


currency_api_key =  "ec255ab3e019e552750c39e7"

url = f'https://v6.exchangerate-api.com/v6/{currency_api_key}/latest/USD'

response = r.get(url)
data = response.json()
new_data = data.get('conversion_rates').keys()
# print(data)
print("We have these currencies available: ") 
formatted_data = tuple(new_data)

print (data)


# # def main():
# #     currency()


# def currency():
#     amount = float(input("Enter Amount:  "))
#     source_currency = input("Enter The currency you have now eg(USD, KSH): ")
#     target_currency  = input("Which currency are you changing to: ")

#     if source_currency and target_currency in 

    


# if __name__ =="__main__":
#     main()

