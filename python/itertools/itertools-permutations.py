from itertools import permutations

s,k = raw_input().split(" ")
for result in list(permutations(sorted(s), int(k))):
    print(''.join(result))
