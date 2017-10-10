import math

n = int(raw_input())
m = 5
share = math.floor(m/2)
like = share
for i in range(1,n):
    share = math.floor(share*3/2)
    like += share
print(int(like))
