from collections import deque

t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    side_lengths = deque(map(int, raw_input().split()))
    current = float('inf')

    while (side_lengths):
        left = side_lengths[0]
        right = side_lengths[-1]
        if (left >= right and left <= current):
            current = side_lengths.popleft()
        elif (left < right and right <= current):
            current = side_lengths.pop()
        else:
            break;

    if (side_lengths):
        print("No")
    else:
        print("Yes")
