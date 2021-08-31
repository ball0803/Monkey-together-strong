'''
Write program by using "for" loop.
First, getting an integer from keyboard (n) to be number of loops.
Then looping to get capital letters for n rounds. After finish looping, displaying number of input characters
which are vowel (A, E, I, O, U).
'''

n = int(input())
vowels = {v for v in 'aeiou'}
ans = 0
for _ in range(n):
    char = input().lower()
    if char in vowels:
        ans += 1

print(ans)
