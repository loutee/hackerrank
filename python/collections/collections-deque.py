from collections import deque

n = int(raw_input())
d = deque()

for i in xrange(n):
    operation = raw_input().split()
    if (operation[0] == "append"):
        d.append(operation[1])
    elif (operation[0] == "appendleft"):
        d.appendleft(operation[1])
    elif (operation[0] == "pop"):
        d.pop()
    else:
        d.popleft()

print(" ".join(str(x) for x in d))
