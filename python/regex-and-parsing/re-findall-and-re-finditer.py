import re

s = raw_input()
vowels = "aeiou"
consonants  = "qwrtypsdfghjklzxcvbnm"
result = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), s, flags = re.I)

if (result):
    print('\n'.join(result))
else:
    print(-1)
