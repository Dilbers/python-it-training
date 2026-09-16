#This program checks if a person is an adult or a teenager based on their age and calculates their age based on the year of birth.
DATE_OF_YEAR = 2026
ADULT_AGE = 18
age = int(input('Enter your age:'))

if age >= ADULT_AGE:
    print('You are adult!')
else:
    print('You are teenager!')

birth_of_year = int(input('Enter your birth of year:'))

print(f"Your age is {DATE_OF_YEAR - birth_of_year}")