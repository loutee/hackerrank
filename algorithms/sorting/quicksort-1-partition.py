#!/bin/python
def partition(ar):
    pivot = ar[0]
    left = []
    right = []
    for i in range(1,len(ar)):
        if (ar[i] < pivot):
            left.append(ar[i])
        else:
            right.append(ar[i])
    print(' '.join(str(x) for x in left) + ' ' + str(pivot) + ' ' + ' '.join(str(x) for x in right))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
