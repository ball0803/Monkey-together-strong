'''
Write a program to get integers m and n, then display a square of m width and length of n.
- The frame of the rectangle is drawn using symbol + (plus).
- The remainder of the rectangular area are filled with the symbol - (minus).
'''

m, n = map(int, input().split())

print('+'*m)
for _ in range(n-2):
    print('+', '-'*(m-2), '+', sep='')
print('+'*m)
