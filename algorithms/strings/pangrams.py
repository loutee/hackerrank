s = raw_input().strip()

s = s.lower()
letters = [0]*26
for i in xrange(len(s)):
    if (s[i] != ' '):
        letters[ord(s[i])-97] = 1

if (sum(letters) == 26):
    print('pangram')
else:
    print('not pangram')
