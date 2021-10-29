def merge_the_tools(string, k):
    substring = list(string[((x-1)*k):x*k] for x in range(1, len(string)//k+1))
    for g in substring:
        a = [k for k in g if k not in a]

        print(''.join(a))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
