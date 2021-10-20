n = int(input('Enter an integer(n): '))
print(f'Summation => {"+".join(str(i) for i in range(1,n+1))} = {sum(i for i in range(1,n+1))}')
