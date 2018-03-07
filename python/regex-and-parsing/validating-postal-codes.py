import re

pattern = re.compile(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$'
)

print(bool(re.match(pattern, raw_input())))
