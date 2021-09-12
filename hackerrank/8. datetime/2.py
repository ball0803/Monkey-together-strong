
from datetime import datetime

def time_delta(t1, t2):
    d1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    d2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    ab = d1 - d2
    return str(abs(int(ab.total_seconds())))
    
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)

