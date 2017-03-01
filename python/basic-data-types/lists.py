if __name__ == '__main__':
    N = int(raw_input())
    list = []

    for _ in range(0, N):
        input = raw_input().split()
        cmd = input[0]
        args = input[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("list." + cmd)
        else:
            print list

