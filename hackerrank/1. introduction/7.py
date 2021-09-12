if __name__ == '__main__':
    n = int(input())
    print(*(digit+1 for digit in range(n)), sep='')
