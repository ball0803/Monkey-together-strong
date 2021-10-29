'''
Write a program to calculate calories for the fruit shop. The program must accept only one order
per time, and the program must run until the user enters 5 to finish the program. The detail of the menu
is as follows.
1 Apple 100 Cal
2 Papaya 120 Cal
3 Banana 200 Cal
4 Orange 60 Cal
5 Exit
When the customer presses 5 to finish the program, the program will show “Bye Bye” message and the
total calories of overall fruits.
'''


MENU = {'1': ('Apple', 100),
        '2': ('Papaya', 120),
        '3': ('Banana', 200),
        '4': ('Orange', 60)}

cart = []
while True:
    i = input()
    if i == '5': 
        break
    cart.append(MENU[i])

total = 0
for name, cal in cart:
    print(f'You choose {name}')
    total += cal
print('Bye Bye')
print(f'Total Calories: {total}')
