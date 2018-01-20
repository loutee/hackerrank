from itertools import groupby

s = raw_input()

result = []

for i,j in groupby(s):
    result.append(tuple([len(list(j)), int(i)]))

print(" ".join(str(x) for x in result))
