from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for key, value in attrs:
                print(f'-> {key} > {value}' )
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for key, value in attrs:
                print(f'-> {key} > {value}' )
                
k = MyHTMLParser()
for _ in range(int(input())):
    k.feed(input().rstrip())
