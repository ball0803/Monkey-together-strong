'''
Write a program to read 2 values from a keyboard for calculating electricity bills.
- take the first character d or h for the type of a building (d stands for dorm, h stands for house)
and
- read the second value as an integer which is the number of power consumption units in that
month
Then calculate the electricity cost using the details in the following table.

                Electricity cost
The number of power                 
consumption units in that           Dorm (d)                    House (h)
month

Less than 200                       2.5 Baht / uinit            1.75 Baht / uinit

200 or more (>= 200)                2.75 Baht / uinit           2.00 Baht / uinit

'''

t = 0 if input() == 'h' else 0.75
unit = int(input())
if unit < 200:
    per_unit = 1.75
else:
    per_unit = 2.00

print(f'{unit * (per_unit + t):.2f}')
