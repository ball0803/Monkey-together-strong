def main():
    operation = input()
    n = int(input())

    original = [input().strip() for _ in range(n)]

    expt_len = len(original[0])
    for row in original[1:]:
        if len(row) != expt_len:
            print('Invalid size')
            return 

    new = []
    if operation == '90':
        for i in range(expt_len):
            new.append([row[i] for row in original[::-1]])
    else:
        for row in original:
            new.append(row[::-1])
        if operation == '180':
            new = new[::-1]

    for row in new:
        print(*(i for i in row), sep='')

if __name__ == '__main__':
    main()
