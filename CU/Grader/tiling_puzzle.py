from typing import List
from itertools import combinations
test = [
    [0,8,7],
    [6,5,4],
    [3,2,1]
    ]

def row_number(t: List[List[int]], e: int) -> int:
    # Iterate through each row 
    for i, row in enumerate(t):
        # Return the row number if 
        if e in row:
            return i

def flatten(t: List[List[int]]) -> List[int]:
    res = []
    for r in t:
        res.extend(r)
    res.remove(0)
    return res

def inversions(t: List[List[int]]) -> int:
    comb = combinations(flatten(t), 2)
    return sum(1 for l, r in comb if l > r)

def solvale(t: List[List[int]]) -> bool:
    if len(t) % 2 == 1:
        return inversions(t) % 2 == 0
    if inversions(t) % 2 == 1:
        return row_number(t, 0) % 2 == 0
    return row_number(t, 0) % 2 == 1

assert row_number(test, 0) == 0
assert flatten(test) == [8,7,6,5,4,3,2,1]
assert inversions(test) == 28
assert solvale(test) == True
print('👌')
