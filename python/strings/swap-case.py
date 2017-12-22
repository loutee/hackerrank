def swap_case(s):
    result = ''
    for i in xrange(len(s)):
        c = ord(s[i])
        if (c >= 65 and c <= 90):
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
