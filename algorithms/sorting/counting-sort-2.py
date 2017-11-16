n = int(raw_input())
ar = map(int, raw_input().split(' '))

count = [0]*(100)
for i in xrange(n):
    count[ar[i]] += 1
sorted = []
for i in xrange(100):
    while (count[i] != 0):
        sorted.append(i)
        count[i] -= 1
print(' '.join(str(x) for x in sorted))
