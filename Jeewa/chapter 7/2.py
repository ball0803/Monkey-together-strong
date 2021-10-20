string = input()
print('Even string = ', *(char for i, char in enumerate(string) if i % 2 == 1), sep='')
