'''
Write a program to receive the amount of money to exchange money. The coins for exchange
consist of 10 baht, 5 baht, 2 baht, and 1 baht coins. For the exchange money program, the highest value
must provide first. Find out how many coins you need to exchange in total.
'''

money = int(input())

for i in (10, 5, 2, 1):
    print(f'{i} baht = {money // i}')
    money %= i
