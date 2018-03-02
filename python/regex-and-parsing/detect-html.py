from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if (attrs):
            for i in xrange(len(attrs)):
                sub = '-> ' + str(attrs[i][0])

                for j in range(1,len(attrs[i])):
                    sub += ' > ' + str(attrs[i][j])
                print(sub)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if (attrs):
            for i in xrange(len(attrs)):
                sub = '-> ' + str(attrs[i][0])

                for j in range(1,len(attrs[i])):
                    sub += ' > ' + str(attrs[i][j])
                print(sub)

n = int(raw_input())
s = ''

for _ in xrange(n):
    s += raw_input()

parser = MyHTMLParser()
parser.feed(s)
