# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        
        for key, value in attrs:
            print(f'-> {key} > {value}' )
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for key, value in attrs:
            print(f'-> {key} > {value}' )

    def handle_comment(self, data: str):
        pass

g = MyHTMLParser()
k = ''
for _ in range(int(input())):
    k = k + input() + '\n'

g.feed(k)
    