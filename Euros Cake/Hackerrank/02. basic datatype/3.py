if __name__ == '__main__':
    n = int(input())
    students = [(input(), float(input())) for _ in range(n)]
    
    score_2nd_lowest = sorted(set(a[1] for a in students))[1]
    print(*sorted(name for name, score in students if score == score_2nd_lowest), sep='\n')
    
