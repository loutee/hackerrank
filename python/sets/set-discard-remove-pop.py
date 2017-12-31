n = int(raw_input())
s = set(map(int, raw_input().split(' ')))
N = int(raw_input())
for _ in xrange(N):
    cmd = raw_input().split(' ')
    if (cmd[0] == 'discard'):
        s.discard(int(cmd[1]))
    elif (cmd[0] == 'remove'):
        s.remove(int(cmd[1]))
    else:
        s.pop()
print(sum(s))
