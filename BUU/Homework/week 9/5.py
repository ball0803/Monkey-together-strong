'''
Write a program to get a positive integer (n), then display n lines of the output. Each line contains
two columns with a space between them. Each column displays the n symbols of ‘>’ or ‘<’ according to
the following conditions.
- if it is an odd numbered line, the first column shows ‘>’ and the second column shows ‘<’.
- if it is an even numbered line, the first column shows ‘<’ and the second column shows ‘>’. 
'''

n = int(input())
for i in range(1, n+1):
    if i % 2 == 1:
        print('>'*n, '<'*n, sep=' ') 
    else:
        print('<'*n, '>'*n, sep=' ') 
