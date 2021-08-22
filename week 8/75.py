'''
Write program by using "for" loop.
First, getting an integer from keyboard (n) to be number of loops.
Then looping to get integers for n rounds. After finish looping, displaying the average as a result on screen
(showing 2-digit precision)
'''

n = int(input())
total = sum(int(input()) for _ in range(n))
print(f'{total / n:.2f}')
