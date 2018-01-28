from collections import Counter

common_three = sorted(list(Counter(raw_input()).most_common(3)))

for i in xrange(3):
    common_char = common_three.pop(common_three.index(max(common_three, key = lambda k: k[1])))
    print(" ".join(str(x) for x in common_char))
