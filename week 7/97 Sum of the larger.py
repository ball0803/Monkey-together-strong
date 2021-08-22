'''
Write a code that first receives one integer (n). Then, the program receives n pairs of integers. The program
outputs the sum of the larger value of each pair.
    Example
Given n = 3. The 3 pairs of integer are (1, 3) (4, 7) and (8, 9)
The larger value of each pair is 3, 7, and 9, respectively.
The sum is 3 + 7 + 9 = 19.

    Input
The first line contains an integer (n).
The second line contains n pairs of integers.

    Output
A single line shows the equations of the sum of the larger value of each pair.
'''

n = int(input())
seq = tuple(map(int, input().split()))
ans = []
for i in range(0, n*2, 2):
    ans.append(max(seq[i], seq[i+1]))
print(f'{" + ".join(str(char) for char in ans)} = {sum(ans)}')

