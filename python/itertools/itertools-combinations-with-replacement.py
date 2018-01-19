from itertools import combinations_with_replacement

s,k = raw_input().split(" ")
s = sorted(s)
k = int(k)

for result in list(combinations_with_replacement(s, k)):
    print("".join(x for x in result))
