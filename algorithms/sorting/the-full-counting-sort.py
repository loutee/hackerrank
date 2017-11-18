n = int(raw_input())
ar = []
for i in xrange(n):
    ar.append(raw_input().split(' '))
    if (i<n/2):
        ar[-1][1] = '-'

words = []
for i in xrange(100):
    words.append([])

for i in xrange(len(ar)):
    words[int(ar[i][0])].append(str(ar[i][1]))
sorted = []
for i in xrange(100):
    while (words[i] != []):
        sorted.append(words[i][0])
        words[i].pop(0)
print(' '.join(str(x) for x in sorted))
