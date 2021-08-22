'''
The village where the little rabbit lives It is believed that numbers that end in 9 or 7 are magical numbers.
Write a program to get the range of numbers that the user enters and print all the magic numbers in this
range.
An input data contains two numbers of the numeric range that are interest, the beginning and the end
(first and last digits are considered Include in the interest range). For example, the input numbers 14 and
29 that means type a magical number from 14 to 29.
Output: First line, type all the magic numbers in the specified range with each number is separated by a
space.
'''

a, b = map(int, input().split())
ans = (i for i in range(a, b+1) if str(i)[-1] == '9' or i % 7 == 0)
print(*ans, sep=' ')


