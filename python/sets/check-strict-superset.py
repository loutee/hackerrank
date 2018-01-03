A = set(raw_input().split(' '))
n = int(raw_input())
result = True
for _ in xrange(n):
    N = set(raw_input().split(' '))
    result = result and A.issuperset(N)
print(result)
