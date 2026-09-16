# This is a simple program that collects user information and calculates the total cost of selected products.
number_of_students = int(input('Enter number of students: '))

user_information = {'name':[], 'age':[], 'location': []}

for i in range(number_of_students):
    user_name = input('Enter your name: ')
    user_age = int(input('Enter your age: '))
    user_location = input('Enter your location: ')

    user_information['name'].append(user_name)
    user_information['age'].append(user_age)
    user_information['location'].append(user_location)


for i in range(len(user_information['name'])):
    print(f'Merhaba {user_information['name'][i]}, {user_information['age'][i]} yasindasin ve {user_information['location'][i]} yasiyorsun.')
