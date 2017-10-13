import math

t = int(raw_input())
for i in xrange(t):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    min = int(math.floor(math.sqrt(a)))
    max = int(math.floor(math.sqrt(b)))
    count = 0
    for j in range(min, max+1):
        square = j*j
        if (square >= a and square <= b):
            count += 1
    print(count)
