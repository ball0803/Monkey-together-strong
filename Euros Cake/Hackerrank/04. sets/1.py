def average(array):
    k = set(array)
    return sum(k) / len(k)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
