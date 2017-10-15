n = int(raw_input())
a = map(int,raw_input().strip().split(' '))

freq = [0]*101
for i in xrange(n):
    freq[a[i]] += 1
print(sum(freq)-max(freq))
