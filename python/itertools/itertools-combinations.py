from itertools import combinations

s,k = raw_input().split(" ")
s = sorted(s)
k = int(k)
for i in range(1, k+1):
    for result in list(combinations(s, i)):
         print("".join(result))
