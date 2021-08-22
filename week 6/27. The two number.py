'''
At the house of the girl and the boy, both of them are doing math homework. Write a program to help
them do the math homework.
Input
First two line: two numbers (which are considered as the first and second operands respectively)
Third line: an integer (an option of the program as explain below)
option 1: do an addition
option 2: do a subtraction
option 3: do a multiplication
option 4: do a division
option 5: do a Mod (%)
option 6: do a power
option 7: calculate an average
other options, the program should display Error
Output
The result of the calculation.
Note: The output should show 5 decimal places (unless pressing 5, the mod will display an integer result).
'''

a = float(input())
b = float(input())
oper_select = int(input()) - 1
oper = (*(o for o in '+-*/%'), '**')
if 5 >= oper_select >= 0:
    print(f"{eval(f'a {oper[oper_select]} b'):.5f}")
elif oper_select == 6:
    print(f'{(a+b)*0.5:.5f}')
else:
    print('Error')
