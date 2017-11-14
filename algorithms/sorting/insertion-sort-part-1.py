#!/bin/python
def insertionSort(ar):
    j = len(ar)-1
    key = ar[j]
    while (j>0 and ar[j-1]>key):
        ar[j] = ar[j-1]
        j -= 1
        print(' '.join(str(x) for x in ar))
    ar[j] = key
    print(' '.join(str(x) for x in ar))


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
