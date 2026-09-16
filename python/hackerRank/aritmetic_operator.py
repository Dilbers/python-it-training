__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
#
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.


a = int(input())
b = int(input())

if a >= 1 and b >= 1 and a <= 10**10 and b <= 10**10:
    print(a + b)
    print(a - b)
    print(a * b)
else:
    print("Please enter numbers greater or equal to 1 and less than or equal to 10^10.")