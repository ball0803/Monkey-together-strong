#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase
def solve(s):
    a = []
    print(list(s.split(' ')))
    for i in list(s.split(' ')):
        print(i)
        if i :
            if i[0] in ascii_lowercase:
                a.append(i.title())
            else:
                a.append(i)
        else:
            a.append('')

    return ' '.join(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
