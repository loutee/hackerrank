#!/bin/python
def insertionSort(ar):
    i = 1
    while (i < len(ar)):
        j = i
        while (j > 0 and ar[j-1] > ar[j]):
            temp = ar[j-1]
            ar[j-1] = ar[j]
            ar[j] = temp
            j -= 1
        i += 1
        print(' '.join(str(x) for x in ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
