def print_rangoli(size):
    row = (2*size)-1
    col = (row * 2) - 1
    
    charater = size + 96

    #ascending
    for i in range(1, (row//2)+1):
        in_row = []
        for x in range(i):
            in_row.append(chr(charater-x))
        for x in reversed(range(i-1)):
            in_row.append(chr(charater-x))
        print(('-'.join(in_row)).center(col, '-'))

    in_row = []
    for x in range(size):
        in_row.append(chr(charater-x))
    for x in reversed(range(size-1)):
        in_row.append(chr(charater-x))
    print(('-'.join(in_row)).center(col, '-'))

    for i in reversed(range(1, (row//2)+1)):
        in_row = []
        for x in range(i):
            in_row.append(chr(charater-x))
        for x in reversed(range(i-1)):
            in_row.append(chr(charater-x))
        print(('-'.join(in_row)).center(col, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
