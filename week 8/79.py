'''
Write a program to get number of students (N). Then loop for N rounds to get score of each student and
find the highest, lowest and average score (average will be shown with 2-digit precision).
'''

n = int(input())
seq = tuple(map(int, input().split()))
print(max(seq))
print(min(seq))
print(f'{sum(seq) / n:.2f}')
