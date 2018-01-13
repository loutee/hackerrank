from itertools import product

a = map(int, raw_input().split(' '))
b = map(int, raw_input().split(' '))

print(' '.join(str(x) for x in list(product(a, b))))
