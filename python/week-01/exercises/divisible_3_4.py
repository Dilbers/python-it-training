#between 1 and 100, print all numbers that are divisible by both 3 and 4
for i in range(1,101):
    if i % 3 == 0 and i % 4 == 0:
        print(f'{i} is divisible 3 and 4')