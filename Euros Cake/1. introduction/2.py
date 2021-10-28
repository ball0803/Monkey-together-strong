if __name__ == '__main__':
    n = int(input())
    
    if n % 2 == 1:
        print('Weird')
    else:
        if n <= 4:
            print('Not Weird')
        elif n <= 20:
            print('Weird')
        else:
            print('Not Weird')
