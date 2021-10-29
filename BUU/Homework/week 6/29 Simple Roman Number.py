'''
Write a program to read an integer (should be 1-9) and print the Roman number of that digit.
The input must be 1 digit number only to output the Roman numerals. In other cases the program will
show results as follows.
In case that user enters negative values, the program shows “Error : Please input positive number”.
In case that user enters positive values that are out of the defined range (1-9), the program shows
“Error : Out of range”.
'''

n = int(input())

if n < 0:
    print('Error : Please input positive number')
elif 1 <= n <= 3:
    print('I' * n)
elif n == 4:
    print('IV')
elif  5 <= n <= 8:
    print('V', 'I'*(n-5), sep='')
elif n == 9:
    print('IX')
elif n == 10:
    print('X')
else:
    print('Error : Out of range')
