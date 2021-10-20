n  = int(input())
print(f'Summation => {"+".join(str(i) for i in range(2, n+1, 2))} = {sum(i for i in range(2, n+1, 2))}')
