# Select Products and Calculate Total Cost
products = {"apple": 3, "banana":5, "bread":2, "milk":4}
basket = []
total = 0
print('Give me 3 product name!')

nth_product = 1
while nth_product <= 3:
    product = input(f'Enter {nth_product}.product name: ')
    if product in products:
        basket.append(product)
        total += products[product]
        nth_product +=1
    else:
        print(f'We dont have {product}')

print(f'your basket:{", ".join(basket)} and total cost:{total}')