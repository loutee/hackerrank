import re

def fun(s):
    pattern = re.compile('^([a-zA-Z0-9-_]+)@([a-zA-Z0-9]+)\.([a-z]{1,3})$')
    if (re.match(pattern, s)):
        return True

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
