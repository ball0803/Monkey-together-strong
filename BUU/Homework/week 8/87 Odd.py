'''
Write a program to get two integers (a and b) and then proceed as follows:
1) Find all the odd numbers between a and b (including a and b) then display the result on the screen
and separate each number with a space.
2) Find the sum of all the odd numbers from 1) and display the result on the screen.
Input:
A single line representing the two integers (a and b) separated by a space.
Output:
The first line shows all the odd numbers between a and b (including a and b).
The second line shows the sum of all odd numbers.
'''
a, b = map(int, input().split())
if a % 2 == 0:
    a += 1

if b % 2 == 1:
    b += 1
print(*(i for i in range(a, b, 2)), sep=' ')
print(sum((i for i in range(a, b, 2))))

