'''
Write a program to receive product information.
1) The number of products (Unit) is an integer.
2) Price per unit (Price / Unit) is a real number.
3) Member status ‘y’ for membership and ‘n’ for non-member case.
The value for calculating program
- Total
- Discount
- Amount
The conditions of the discount as follows
1. If you are a member (Member = y)
Condition
If the total amount is not more than 500, 10% discount of the total amount.
If the total amount is more than 500 but less than 1000, 15% discount of the total amount.
If the total amount (Total) 1000 or more, 20% discount of the total amount.
2. If not a member (Member = n)
Condition
If the total amount is not more than 500, 5% discount of the total amount.
If the total amount is more than 500 but less than 1000, 10% discount of the total amount.
If the total amount (Total) 1000 or more, 15% discount of the total amount.
Note The display of the result is displayed as a 2 decimal number with the text as in the example below
'''

pieces = int(input())
per_piece = float(input())
discount = 0.05 if input() == 'y' else 0

total = pieces * per_piece

if total <= 500:
    discount  += 0.05
elif 500 < total <= 1_000:
    discount += 0.1
else:
    discount += 0.15

print(f'Total {total:.2f}')
print(f'Discount {total * discount:.2f}')
print(f'Amount {total * (1 - discount):.2f}')
