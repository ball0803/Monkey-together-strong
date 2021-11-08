arr = list(map(int, input().split()))
mean = sum(arr) / len(arr)
arr.sort()
median_index = (len(arr) / 2) - 1
print(mean)
print(arr)
if median_index.is_integer():
    print((arr[int(median_index)]+arr[int(median_index)+1])/2)
else:
    print(arr[int(median_index)])
