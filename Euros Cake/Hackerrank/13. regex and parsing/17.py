import re
n, m = map(int, input().rstrip().split())

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decode = ''
for chars in zip(*matrix):
    decode += ''.join(chars)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", decode))

