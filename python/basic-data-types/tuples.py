if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    for i in range(0,n):
        t = tuple(integer_list)
    print hash(t)
