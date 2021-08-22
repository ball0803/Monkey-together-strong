'''
Write a program that reads three numbers and prints “increasing” if they are in increasing order,
“decreasing” if they are in decreasing order, and “neither” otherwise. Here, “increasing” means “strictly
increasing”, with each value larger than its predecessor. The sequence 3 4 4 would not be considered
increasing
'''

a = int(input())
b = int(input())
c = int(input())

if c > b > a:
    print('increasing')
elif a > b > c:
    print('decreasing')
else:
    print('neither')
