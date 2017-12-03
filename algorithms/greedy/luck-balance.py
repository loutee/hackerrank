n,k = raw_input().split(' ')
n,k = [int(n),int(k)]

contests = []
for _ in xrange(n):
    contests.append(map(int, raw_input().split(' ')))
contests = sorted(contests,reverse=True)
luck = 0
while(contests != []):
    if (contests[0][1] == 0):
        # Lose game
        luck += contests[0][0]
    else:
        if (k>0):
            # Lose game, decrement k
            luck += contests[0][0]
            k -= 1
        else:
            # Win game
            luck -= contests[0][0]
    contests.pop(0)
print(luck)
