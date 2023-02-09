from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = []

    def handle_starttag(self, tag, attrs):
        self.collection.append((tag, attrs))


url = 'https://greenatom.ru/'
f = urllib.request.urlopen('http://www.python.org/')
html = f.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(html)

tags = parser.collection
tags_without_attrs = [tag for tag in tags if len(tag[1]) > 0]


def run():
    print(f"В коде главной страницы сайта greenatom.ru содержится {len(tags)} HTML-тегов")
    print(f"Из них {len(tags_without_attrs)} содержат атрибуты")


if __name__ == '__main__':
    run()
