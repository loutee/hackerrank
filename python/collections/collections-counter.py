from collections import Counter

x = int(raw_input())
shoeSizes = map(int, raw_input().split())
n = int(raw_input())

availShoes = Counter(shoeSizes)
profit = 0

for _ in xrange(n):
    customerSize, price = map(int, raw_input().split(" "))

    if (availShoes[customerSize] > 0):
        availShoes[customerSize] -= 1
        profit += price

print(profit)
