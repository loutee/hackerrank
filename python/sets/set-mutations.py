lenA = int(raw_input())
A = set(map(int, raw_input().split(' ')))
N = int(raw_input())
for _ in xrange(N):
    cmd = raw_input().split(' ')
    inset = set(map(int, raw_input().split(' ')))
    if (cmd[0] == 'update'):
        A.update(inset)
    elif (cmd[0] == 'intersection_update'):
        A.intersection_update(inset)
    elif (cmd[0] == 'difference_update'):
        A.difference_update(inset)
    elif (cmd[0] == 'symmetric_difference_update'):
        A.symmetric_difference_update(inset)
print(sum(A))
