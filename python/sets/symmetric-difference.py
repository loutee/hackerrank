m = int(raw_input())
a = set(map(int, raw_input().split(' ')))
n = int(raw_input())
b = set(map(int, raw_input().split(' ')))
result = sorted(list(a.difference(b).union(b.difference(a))))
for i in xrange(len(result)):
    print(result[i])
