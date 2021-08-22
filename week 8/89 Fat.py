'''
Write a program that counts fat and thin people. The program will receive numbers representing the
weight of the user from the keyboard until -1 or cover ten numbers of the weight have been entered (this
problem has 2 conditions to stop receiving data: 1) data received as -1 and 2) receive the weight complete
10 values).
Then show the number of obese people and thin people that were considered by the following criteria.
- If the weight is more than 60 Kg then it will be fat.
- Otherwise, it is considered a thin person.
Input:
N lines that each line represents weight data.
Output:
The first line shows the number of obese people.
The second line shows the number of thin people.
'''

total = 0
fat = 0
while total <= 10:
    n = int(input())
    if n == -1:
        break
    if n > 60:
        fat +=1
    total += 1

print(fat)
print(total - fat)
