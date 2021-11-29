cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',

    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',

    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',

    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',

    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}

to_decrypt = tuple(input())
res = ''
for i in range(0, len(to_decrypt), 2):
    
    current_pair = (to_decrypt[i], to_decrypt[i+1])

    value = cipher_key.get(current_pair, -1)
    if value == -1:
        print("FAILED TO DECRYPT")
        break
    res = f'{res}{value}'
else:
    print(res)
