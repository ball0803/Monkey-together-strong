scores = []
for i in range(1, 11):
    current = float(input(f'Please enter score#{i}: '))
    if 100 >= current >= 0:
        scores.append(current)

print(f"Amount of scores : {len(scores)}")
print(f'Average Score : {sum(scores)/len(scores)}')
print(f'Highest Score : {max(scores)}')
print(f'Lowest Score : {min(scores)}')
print('======================')
print(f"Total Passed Student : {sum(1 for i in scores if i >= 50)}")
print(f'Average Passed score : {sum(i for i in scores if i >= 50)/sum(1 for i in scores if i >= 50)}')
print('======================')
print(f'Scores list: {sorted(scores, reverse=True)}')
