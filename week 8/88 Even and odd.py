'''
Write a program to continuously get an integer numbers until you enter -1 and then counting the total
odd numbers and total even numbers of numbers that user has entered.
Input:
N line represents all the input that needs to be checked
Output:
The first line shows the total odd numbers of the considered input.
The second line shows the total even numbers of the considered input.
'''

total = -1
even = 0
k = 0
while k != -1:
    n = int(input())
    if n % 2 == 0:
        even += 1
    total += 1
    k = n
print(total - even)
print(even)
