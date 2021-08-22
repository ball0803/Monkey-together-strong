'''
Write a code that determine the sum ∑ 1
�
�
�=1 . The only input for this program is an integer, n. For
the example, if n = 2, the output would be 1.5:
∑ 1
�
2
�=1 =
1
1
+ 1
2 = 1.5
Input
A single line contains a positive integer, n.
Output
A single line contains the value of the sum (rounded to 4 decimal places) according to the formula,
∑ 1
�
�
�=1 .
'''

n = int(input())
ans = sum((1/i) for i in range(1, n+1))
print(f'{ans:.4f}')
