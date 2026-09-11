__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"
#Practice input, type conversion, and conditions.
# -Ask the user for their age.
# -If under 18 → print “You are not an adult”.
# -Else → print “You are an adult”.
# -Ask for birth year and calculate age (use 2025).

user_age = None
ADULT_AGE = 18
birth_day_year = None
CURRENT_YEAR = 2025

while True:
    user_age = input("What is your age?: ")
    if user_age.isdigit():
        user_age = int(user_age)
        break
    print("It isn't valid. Please enter number!")

if(user_age < ADULT_AGE):
    print("You are not an adult!")
else:
    print("You are an adult!")

while True:
    birth_day_year = input("What is your year of birth?: ")
    if birth_day_year.isdigit():
        birth_day_year = int(birth_day_year)
        break
    print("It isn't valid. Please enter number!")

user_age = CURRENT_YEAR - birth_day_year

print(f"Your age: {user_age} in {CURRENT_YEAR}!")