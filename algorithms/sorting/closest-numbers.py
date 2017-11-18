def quicksort(a):
	if(len(a)<2):
		return a
	else:
		pivot = a[0]
		smaller = []
		bigger = []
		for i in a[1:]:
			if i<pivot:
				smaller.append(i)
			else:
				bigger.append(i)
	return quicksort(smaller)+[pivot]+quicksort(bigger)

n = int(raw_input())
ar = map(int, raw_input().split(' '))
sorted = quicksort(ar)
min = abs(sorted[1]-sorted[0])
for i in range(2,n):
    diff = abs(sorted[i]-sorted[i-1])
    if (diff < min):
        min = diff

result = []
for i in xrange(n):
    diff = abs(sorted[i]-sorted[i-1])
    if (diff == min):
        result.append(sorted[i-1])
        result.append(sorted[i])
print(' '.join(str(x) for x in result))
