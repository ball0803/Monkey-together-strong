s = input()
lower = ''
upper = ''
odd = ''
even = ''
for char in s:
    if char.islower():
        lower += char
    elif char.isupper():
        upper += char
    else:
        if int(char) % 2 == 1:
            odd += char
        else:
            even += char

s_sorted = ''
for p in  map(sorted, (lower, upper, odd, even)):
    s_sorted += ''.join(p)
print(s_sorted)
