n,m = raw_input().split(' ')
n,m = [int(n),int(m)]
arr = map(int, raw_input().split(' '))
a = set(map(int, raw_input().split(' ')))
b = set(map(int, raw_input().split(' ')))
happiness = 0
for i in xrange(n):
    if (arr[i] in a):
        happiness += 1
    elif (arr[i] in b):
        happiness -= 1
print(happiness)
