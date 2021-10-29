'''
Write a program to get one positive integer (N), then find out if any positive integers from N to 0 are
divisible by 10 and display them on the screen.
Input:
Gets one positive integer N on a single line.
Output:
Shows a positive integers from N to 0 that is divisible by 10 (separate each number with a space).
'''

n = int(input())
if n % 10 != 0:
    n -= n % 10
print(*(i for i in range(n, -1, -10)))
