cube = lambda x: x**3

def fibonacci(n):
    if (n >= 2):
        result = [0,1]
        for _ in xrange(n-2):
            result.append(result[-2] + result[-1])
        return result

    elif(n == 1):
        return [0]

    else:
        return []

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
