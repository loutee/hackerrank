if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    nums = set(arr)
    nums.discard(max(nums))
    print(max(nums))
