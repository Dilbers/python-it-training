#This program determines if a number is even or odd.
number = int(input('Enter number to determine even or odd:'))

if number == 0:
    print("Number is zero.")
elif number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")