if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(1, n+1):
        
        if i == ((n-1)//2)+1:
            print('WELCOME'.center(m, '-'))

        elif i < ((n-1)//2)+1:
            print(('.|.'*((i*2)-1)).center(m, '-'))
        
        else:
            print(('.|.'*(((n - i+1)*2)-1)).center(m, '-'))
        
