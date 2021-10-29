'''
The original U.S. income tax of 1913 was quite simple. The tax was
1 percent on the first $50,000.
2 percent on the amount over $50,000 up to $75,000.
3 percent on the amount over $75,000 up to $100,000.
4 percent on the amount over $100,000 up to $250,000.
5 percent on the amount over $250,000 up to $500,000.
6 percent on the amount over $500,000.
There was no separate schedule for single or married taxpayers. Write a program that computes the
income tax according to this schedule. (Display the result in 2 decimal places.)
'''

income = int(input())
tax = 0
if 50_000 >= income:
    print(f"{income * 0.01:.2f}")
else:
    tax += 50000 * 0.01
    income -= 50000

    if 25000 >= income > 0:
        print(f'{(income * 0.02) + tax:.2f}')
    else:
        tax += 25000 * 0.02
        income -= 25000

        if 25000 >= income > 0:
            print(f'{(income * 0.03) + tax:.2f}')
        else:
            tax += 25000 * 0.03
            income -= 25000

            if 150000 >= income > 0:
                print(f'{(income * 0.04) + tax:.2f}')
            else:
                tax += 150000 * 0.04
                income -= 150000

                if 250000 >= income > 0:
                    print(f'{(income * 0.05) + tax:.2f}')
                else:
                    tax += 250000 * 0.05
                    income -= 250000
                    print(f'{(income * 0.06) + tax:.2f}')
