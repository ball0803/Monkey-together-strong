def wrap(string, max_width):
           
    return '\n'.join([string[(max_width*i):(max_width*(i+1))] for i in range(len(string))])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
