#This program calculates the Body Mass Index (BMI) based on the user's height and weight, and categorizes the result into different weight categories.
height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print('Thin')
elif bmi >= 18.5 and bmi < 25:
    print('Normal')
elif bmi >= 25 and bmi < 30:
    print('Overweight')
else:
    print('Obese')