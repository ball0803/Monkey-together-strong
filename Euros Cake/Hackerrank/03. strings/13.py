import re
def minion_game(string):
    vowels = re.compile('^[AEIOU]')
    p_v = 0
    p_c = 0
    
    for x_i in range(len(string)):
        if vowels.match(string[x_i]):
            p_v += (len(string)-x_i)
        else:
            p_c += (len(string)-x_i)

    if p_c > p_v:
        print(f'Stuart {p_c}')
    elif p_c < p_v:
        print(f'Kevin {p_v}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
