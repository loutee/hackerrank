#!/bin/python
def insertionSort(ar):
    i = 1
    prev = ar[0]
    while (i < len(ar)):
        j = i
        if (ar[i] > prev):
            prev = ar[i]
        else:
            temp = ar[i]
            while (j > 0 and not (ar[j-1] < temp and ar[j] >= temp)):
                ar[j] = ar[j-1]
                j -= 1
                print(' '.join(str(x) for x in ar))
            ar[j] = temp
            print(' '.join(str(x) for x in ar))
        i += 1

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
