_ = input()
a = {i for i in map(int, input().rstrip().split())}
_ = input()
b = {i for i in map(int, input().rstrip().split())}

print(*sorted(a.symmetric_difference(b)), sep='\n')
