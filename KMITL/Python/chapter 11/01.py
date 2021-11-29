from string import ascii_uppercase

APLHABET = tuple(char for char in ascii_uppercase) # = ("A", "B", "C", "D", ...)

n  = int(input())
for row in range(1, n+1):
    this_row = ' '.join(APLHABET[0:row])
    print(this_row)
