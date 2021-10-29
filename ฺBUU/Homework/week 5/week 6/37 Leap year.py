import calendar

'''
A year with 366 days is called a leap year. A year is a leap year if it is divisible by four (for example, 1980),
except that it is not a leap year if it is divisible by 100 (for example, 1900); however, it is a leap year if it is
divisible by 400 (for example, 2000). There were no exceptions before the introduction of the Gregorian
calendar on October 15, 1582 (1500 was a leap year). Write a program that asks the user for a year and
computes whether that year is a leap year.
'''

y = int(input())
if calendar.isleap(y):
    print(f'{y} is a leap year')
else:
    print(f'{y} is not a leap year')
