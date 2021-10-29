arr = [float(input(f'Please enter score#{i}: ')) for i in range(1, 11) ]
scores_okay = tuple(score for score in arr if 100 >= score >= 0)

print(f'''\
Amount of Score : {len(scores_okay)}
Average Score : {sum(scores_okay)/len(scores_okay)}
Highest Score : {max(scores_okay)}
Lowest Score : {min(scores_okay)}
======================
Total Passed Student : {sum(1 for i in scores_okay if i >= 50)}
Average Passed score : {sum(i for i in scores_okay if i >= 50)/sum(1 for i in scores_okay if i >= 50)}
======================
Scores list: {sorted(scores_okay, reverse=True)}''')
