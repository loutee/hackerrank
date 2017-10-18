p = int(raw_input())
q = int(raw_input())

result = []
for i in range(p,q+1):
    k = str(i*i)
    left = k[0:(len(k)/2)]
    if (left == ""):
        left = "0"
    right = k[(len(k)/2):]
    if (right == ""):
        right = "0"
    total = int(left)+int(right)
    if (total == i):
        result.append(str(i))
if (len(result) == 0):
    print("INVALID RANGE")
else:
    print(" ".join(result))
