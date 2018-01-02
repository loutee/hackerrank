k = int(raw_input())
rnum = map(int, raw_input().split(' '))
track = set()
dels = set()
for i in xrange(len(rnum)):
    if (rnum[i] not in track):
        track.update([rnum[i]])
    else:
        dels.update([rnum[i]])
print(''.join(str(x) for x in track.difference(dels)))
