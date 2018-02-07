n = int(raw_input())
raw_arr = raw_input().split()

pos_arr = map(lambda x: int(x) >= 0, raw_arr)
pal_arr = map(lambda x: x == x[::-1], raw_arr)

print(all(pos_arr) and any(pal_arr))
