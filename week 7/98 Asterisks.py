'''
Write a code to receive an integer (n). Then, the code outputs the three lines as follows:
- 1st line shows n of *.
- 2nd line shows (n-2) of *. (If n-2 is less than 1, no need to output any asterisks.)
- 3rd line shows (n-4) of *. (If n-4 is less than 1, no need to output any asterisks.)
    Input
An integer (n).
    Output
1st line shows n of *.
2nd line shows (n-2) of *. (If n-2 is less than 1, no need to output any asterisks.)
3rd line shows (n-4) of *. (If n-4 is less than 1, no need to output any asterisks.)
'''

n = int(input())
c = 3
while c > 0 and n > 0:
    print('*'*n)
    n -= 2
    c -= 1
     
