'''
Write a program to read an integer (the values are from 10 to 99) and read one character which is a plus
or multiply sign. Create a new number by rearranging each input digit from left to right. Then bring the
previous numbers to add or multiply with the swapped numbers. The program should show the result as
in the example below (There is a space before and after the + and = signs)
'''


num = input()
op = input()
r = ''.join(char for char in reversed(num))

print(f'{num} {op} {r} = {eval(f"{num} {op} {r}")}')
