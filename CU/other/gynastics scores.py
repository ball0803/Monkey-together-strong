'''
restriction -> no min(), max() if else only
'''

arr = list(map(float, input().split()))
arr.sort()
print(round(sum(arr[1:3])/2, 2))
