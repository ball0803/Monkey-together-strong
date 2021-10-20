arr = list(map(float, input().split()))
min_val = arr[0]
for val in arr[1:]:
    if val < min_val:
        min_val = val

if min_val.is_integer():
    min_val = int(min_val)

print(f'Min value {min_val}')
