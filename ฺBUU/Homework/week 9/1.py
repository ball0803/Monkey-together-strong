'''
Write a program to get one input of the positive integer number and then display the result of
calculating the factorial value (The factorial value is the product of numbers from 1 to n, for example, 5!
= 5 * 4 * 3 * 2 * 1 = 120)
Input
one line of code --> Represents the number to calculate the factorial value.
Output
one line of code --> Shows the result of factorial value. 
'''
def factorial(n: int) -> int:
    x = 1
    for i in range(1, n+1):
        x *= i
    return x
    
n = int(input())
print(factorial(n))
