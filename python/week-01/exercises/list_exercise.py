# List Exercise
students = ['Ali','Ayse','Mehmet']
ages = ['14','15','14']

for i in range(len(ages)):
    print(f'{students[i]} - {ages[i]} yasinda')

students.append(input('Enter student name: '))
ages.append(input('Enter student age: '))

print('--------------NEW LIST--------------')
for i in range(len(ages)):
    print(f'{students[i]} - {ages[i]} yasinda')

students.remove('Ali')
ages.remove('14')

name = students.pop(0)
age = ages.pop(0)

print('--------------NEW LIST--------------')
for i in range(len(ages)):
    print(f'{students[i]} - {ages[i]} yasinda')

print(f'Giden Ogrenci:{name} - yas {age}')