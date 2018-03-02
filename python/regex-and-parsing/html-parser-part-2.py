from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if ("\n" in comment):
            print(">>> Multi-line Comment\n" + comment)
        else:
            print(">>> Single-line Comment\n" + comment)

    def handle_data(self, data):
        if (data.strip()):
            print(">>> Data\n" + data)


html = ""
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
