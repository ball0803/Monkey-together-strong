'''
Write a program to receive exercise score (out of 10), mid-term score (out of 40), and final score
(out of 50) and report the exam results as follows:
- Students will pass the exam if each score (i.e., exercise, mid-term and final scores) is not lesser than
50%.
'''
a = int(input())
b = int(input())
c = int(input())
print('pass' if a+b+c >= 50 else 'fail')


'''
One-liner sol
print('pass' if sum(map(int, (input(), input(), input()))) >= 50 else 'fail')
'''
