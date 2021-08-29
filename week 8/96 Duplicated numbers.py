'''
Write a code to receive a non-zero integer (S) in focus. Then, the program repeatedly receives
integers (one integer at a time) until the received integer is zero.
The program will output the maximum number of consecutive S, excluding the first S. For
example, if the input is 2 2 2 2 2 3 2 2 2, 2 is the number in focus. The program needs to determine the
number of maximally consecutive "2", excluding the first "2". (For this example, the output must be 4.)
Input
List of integers. The last one is always 0.
Output
The number of maximally consecutive S.
'''

seq = map(int, input().split()[1:])
count = 1
ans = []
for i in range(len(seq)-1):
    if seq[i] == seq[i+1]:
        count += 1
    else:
        ans.append(count)
        count = 1
print(max(ans))
