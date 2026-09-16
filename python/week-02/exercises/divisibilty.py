# This program creates a list of even numbers from 1 to 20 and stores their squares in a new list.
divisible = lambda x, y: x % y == 0

divide_integer = int(input('Divide number: '))
number_dividing_start = int(input(f'Enter a start number to check divisibility from {divide_integer}: '))
number_dividing_end = int(input(f'Enter a end number to check divisibility from {divide_integer}: '))

divisible_numbers = list(filter(lambda x: divisible(x, divide_integer), range(number_dividing_start, number_dividing_end + 1)))

print(divisible_numbers)