'''
Write a program for receiving an integer number (N) as an input, and then output n symbols according to
the following conditions:
- If the position for the output is not divisible by 5, show the symbol *.
- Otherwise, output the symbol X. (Note the uppercase X.)
Example : If N = 6, then all 6 symbols must be shown according to their positions.
- For the positions 1 – 4, the code output the symbol *.
- For the positions 5, the code output the symbol X.
- For the positions 6, the code output the symbol *.
Therefore, the program will output the result of ****X* on the screen.
Input
A single line contains the number of symbols you want displayed on the screen.
Output
A single line shows the symbols according to the specified conditions
'''

n = int(input())
print('****X' * (n // 5), '*'*(n % 5), sep='')
