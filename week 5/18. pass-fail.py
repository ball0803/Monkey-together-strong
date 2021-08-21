'''
Write a program to receive midterm and final scores and then print out the total score with a
message stating that the exam failed or passed as an example (the passing criteria is greater than 50).
'''

a = int(input())
b = int(input())
print(a+b)
print('pass' if a+b > 50 else 'fail')
