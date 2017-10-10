def reverse(s):
    s = str(s)[::-1]
    return int(s)

i,j,k = raw_input().strip().split(' ')
i,j,k = [int(i),int(j),int(k)]
count = 0
for x in range(i,j+1):
    if ((abs(x - reverse(x))) % k == 0):
        count += 1
print(count)
