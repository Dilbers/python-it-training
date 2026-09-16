#This program performs basic arithmetic operations based on user input.
first_number = int(input('Enter a number: '))
second_number = int(input('Enter a number: '))
operator = input('Enter operation as character(+, -, *, /): ')

if operator == '+':
    print(f'Summing result: {first_number + second_number}')
elif operator == '-':
    print(f'Extraction result: {first_number - second_number}')
elif operator == '*':
    print(f'Multipilacion result: {first_number * second_number}')
else:
    print(f'Dividing result: {int(first_number / second_number)}')