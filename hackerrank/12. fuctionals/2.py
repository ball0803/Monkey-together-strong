def fibonacci(n):    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    result = [0, 1]
    for k in range(2, n):
        result.append(result[k-1]+result[k-2])
    return result
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x*x*x, fibonacci(n))))
