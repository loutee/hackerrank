N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
smallest = lists[-1]
index = 0
for i in range(0,N-(K-1)):
    diff = lists[i+K-1]-lists[i]
    if (diff < smallest):
        smallest = diff
        index = i
min_diff = max(lists[index:index+K])-min(lists[index:index+K])
print(min_diff)
