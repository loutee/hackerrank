n = int(raw_input())
p = raw_input()
level = 0
below = False
count = 0
for i in xrange(n):
    if (p[i] == 'U'):
        level += 1
    else:
        level -= 1
    if (level == 0 and below == True):
        count += 1
        below = False
    if (level < 0):
        below = True
print(count)
