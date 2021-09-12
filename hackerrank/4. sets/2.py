from collections import Counter

n, m = map(int, input().rstrip().split())
n_dict = Counter(i for i in map(int, input().rstrip().split()))
set_a = set(i for i in map(int, input().rstrip().split()))
set_b = set(i for i in map(int, input().rstrip().split()))

happiness = 0
for key in n_dict.keys():
    count = n_dict.get(key)
    if key in set_a:
        happiness += count
        
    elif key in set_b:
        happiness -= count
        
print(happiness)
