if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m_a = max(arr)
    print(max((x for x in arr if x < m_a)))
