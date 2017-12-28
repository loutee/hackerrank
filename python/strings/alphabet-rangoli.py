def print_rangoli(size):
    slist = []
    length = 4*size-3
    for i in range(1,size+1):
        s = ('-'.join(chr(x) for x in range(96+size,96+size-i,-1)))
        slist.append(s+s[-2::-1])
        print slist[-1].center(length,'-')
    for i in range(size-2,-1,-1):
        print slist[i].center(length,'-')

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
