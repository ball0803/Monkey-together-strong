def rule(arr: list[int]) -> bool:
    rules = [
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0]
    ]
    return any(arr == rule for rule in rules)

def advance_arr(arr: list[int], generations: int = 20) -> None:
    pn = arr
    for _ in range(generations):
        p0 = pn
        for i in range(2, 18):
            if rule(p0[i-2:i+3]):
                pn[i] = 1
            else:
                pn[i] = 0
        print(*pn, sep='')

def main() -> None:
    #Please type hint your functions
    p0 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    # p0 = list(map(int, input().split()))
    advance_arr(p0)

if __name__ == '__main__':
    main()
