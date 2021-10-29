from sys import stdin, stdout
if __name__ == '__main__':
    n = int(stdin.readline())
    for i in range(n):
        stdout.write(f'{i*i}\n')
