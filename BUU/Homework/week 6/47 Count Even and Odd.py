'''
Write a program to get 3 integers from keyboard, then find out how many even and odd numbers there
are. Finally, print ofor _ in range(3)nd “odd” followed by quantity of the even and odd number.
'''

seq = (int(input()) for _ in range(3))
even = sum(1 for i in seq if i % 2 ==0)
print(f'even {even}', f'odd {3-even}', sep='\n')

