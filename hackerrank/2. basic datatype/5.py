if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        c = input().split()
        met, args = c[0], c[1:]
        
        if met != 'print':
            expression = f"{met}({','.join(args)})"
            eval(f'arr.{expression}')
        else: 
            print(arr)
        
