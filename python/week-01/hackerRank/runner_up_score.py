__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#Input Format
#The first line contains . The second line contains an array   of  integers each separated by a space.
#Constraints
#2<=n<=10
#-100<=A[i]<=100
#Output Format
#Print the runner-up score.
#Sample Input 0
#5
#2 3 6 6 5
#Sample Output 0
#5
#Explanation 0
#Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

nummer_of_participants = int(input())
scrores = set()
arr = map(int, input().split())

if nummer_of_participants < 2 or nummer_of_participants > 10:
    print("Invalid number of participants. Must be between 2 and 10.")
    exit()

for score in arr:
    if score < -100 or score > 100:
        print("Invalid score. Must be between -100 and 100.")
        exit()
    scrores.add(score)

scrores.remove(max(scrores))
print(max(scrores))