n = int(raw_input())
a = map(int, raw_input().split(' '))
m = int(raw_input())
b = map(int, raw_input().split(' '))

a = sorted(a)
b = sorted(b)
missing = []
while (a != [] and b != []):
    if (a[0] == b[0]):
        a.pop(0)
        b.pop(0)
    else:
        missing.append(b.pop(0))
missing = sorted(set(missing+b))
print(' '.join(str(x) for x in missing))
