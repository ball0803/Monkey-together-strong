n, x = map(int, input().split())
scores = list()
for _ in range(x):
    score = map(float, input().split())
    scores.append(score)

for i in zip(*scores):
    print(sum(i)/x)

