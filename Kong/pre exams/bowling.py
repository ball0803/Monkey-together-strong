score_str = input()
n = int(input())

frames = []
for i in score_str:
    if i == 'X':
        frames.append(10)
    elif i == '/':
        frames.append(10-int(frames[-1]))
    else:
        frames.append(int(i))

frame_bonus = []
skip = False
for i, val in enumerate(frames[:-3]):
    if skip:
        skip = False
        continue
    if val == 10:
        frame_bonus.append(10+frames[i+1]+frames[i+2])
    elif val + frames[i+1] == 10:
        frame_bonus.append(10+frames[i+2])
        skip = True
    else:
        frame_bonus.append(val + frames[i+1])
        skip = True
else:
    frame_bonus.append(sum(frames[-3:]))

if n < 1 or n > 10:
    print(sum(frame_bonus))
else:
    print(frame_bonus[n-1])
