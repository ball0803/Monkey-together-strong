'''
Write a program to read 6 integers (y1, m1, d1, y2, m2, and d2)
- y1 m1 and d1 are the year, month and birthday of the first friend
- y2 m2 and d2 are the year, month and second friend's birthday
Write a program to find out which friend was born first. If the first person is born first, print “1”, if the
second friend is born first, print “2” (in case that the birthday of both of them is similar, print “equal”).
'''

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

if y1 != y2:
    print('1' if y1 < y2 else '2')
else:
    if m1 != m2:
        print('1' if m1 < m2 else '2')
    else:
        if d1 != d2:
            print('1' if d1 < d2 else '2')
        else:
            print('equal')
