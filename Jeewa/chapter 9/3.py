arr = tuple(map(int, input()))
ascending = False
descending = False
for i in range(len(arr)):
    if arr[i] > arr[i+1]:
        descending = True
    elif arr[i] < arr[i+1]:
        ascending = True
    if descending and ascending:
        print('not acsending or descending')
        break
else:
    print('acsending' if ascending else 'descending')
