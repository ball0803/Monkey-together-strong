'''
Write the code that receives 2 integers: the starting integer (s) and the finishing integer (f). Then, the
program outputs the sum of the odd integers between s and f.
Input
The 1st line contains the starting integer (s).
The 2nd line contains the finishing integer (f).
Output
The 1st line contains all the integers between s and f.
The 2nd line contains the sum of the odd integers between s and f.
'''

s = int(input())
f = int(input())

print(*(i for i in range(s, f+1)))

if s % 2 == 0:
    s += 1
else:
    s += 2

if f % 2 == 1:
    f -= 2
print(sum(i for i in range(s,f,2)))

