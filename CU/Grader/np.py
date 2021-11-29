from random import random
from math import e

def p(x):
    def logit(x_one, x_two):
        # change this part to NumPy
        exp = -3.98 + (0.1 * x_one) + (0.5 * x_two)
        return  1 / (1 + (e ** -(exp)))

    return [*map(lambda y: logit(y[0], y[1]), x)]
