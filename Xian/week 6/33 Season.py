'''
The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a given month and day.
The month 1, 2, 3 are Winter
The month 4, 5, 6 are Spring
The month 7, 8, 9 are Summer
The month 10, 11, 12 are Fall
However, the season changes after the 21st of the month that is divisible by 3, going from Winter to
Spring, from Spring to Summer, from Summer to Fall, and from Fall to Winter.
'''


m = int(input())
d = int(input())

season = ('Winter', 'Spring', 'Summer', 'Fall')
if m % 3 != 0:
    print(season[m // 3])
else:
    print(season[m // 3] if d >= 21 else season[(m // 3) - 1])
