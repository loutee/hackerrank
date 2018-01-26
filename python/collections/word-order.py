from collections import Counter, OrderedDict

dict = OrderedDict()

for i in xrange(int(raw_input())):
    word = raw_input()
    try:
        dict[word] += 1
    except:
        dict[word] = 1

print(len(dict))
print(" ".join(str(x[1]) for x in dict.items()))
