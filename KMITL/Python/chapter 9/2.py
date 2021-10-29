arr = input().split()
for i in range(len(arr)):
    arr[i] = f'{arr[i]}{i+1}'
print(arr)
