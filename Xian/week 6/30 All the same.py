'''
Write a program that reads three numbers and prints “all the same” if they are all the same, “all
different” if they are all different, and “neither” otherwise.
'''

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('all the same')
elif a != b != c:
    print('all different')
else:
    print('neither')
