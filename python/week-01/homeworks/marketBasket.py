__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

#Practice dictionaries and loops.
#Products and prices:
#-products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
#Ask the user for 3 products.
#Calculate total price.
#Print:
#-Your basket: apple, banana, milk
#-Total price: 12 TL
#-If a product doesn’t exist → print warning.
import re

index = 0
total_price = 0
products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}

basket = input('Enter three product that you wanna buy: ')

basket_list = basket.strip().lower().split()

for i in basket_list:
    basket_list[index] = re.sub(r'[^a-zA-Z0-9]+', '', i)
    index+=1

for i in basket_list:
    if(i in products):
        total_price += products[i]
    else:
        print(f"\033[93m[Warning] The product {i} doesn’t exist!\033[0m")

print(f'Total price: {total_price} TL')