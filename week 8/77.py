'''
Write program to get integer N which is number of data. Then looping for N rounds to get integer input
and showing result as summation of all N data on screen
'''

n = int(input())
ans = sum(int(input()) for _ in range(n))
print(ans)
