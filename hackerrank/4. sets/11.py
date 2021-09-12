_ = int(input())
rooms = map(int, input().split())
single = set()
multiple = set()
for room in rooms:
    if room in single:
        multiple.add(room)
    else:
        single.add(room)

print(*single.difference(multiple))
