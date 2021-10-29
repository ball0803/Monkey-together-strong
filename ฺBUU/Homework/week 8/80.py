'''
Write a program to get number of loops (N). Then loop for N rounds to get numbers and find how many
zero input.
'''
_ = input()
k = map(int, input().split())
ans = 0
for i in k:
    if i == 0:
        ans += 1
    
print(ans)
