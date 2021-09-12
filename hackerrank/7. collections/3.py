from collections import namedtuple
from statistics import mean
n = int(input())
w = input().split()

student = namedtuple('s', w)

total_marks = []
for _ in range(n):
    a, b, c, d = input().rstrip().split()
    current = student(a,b,c,d)
    total_marks.append(int(current.MARKS))
print(f'{mean(total_marks):.2f}')
