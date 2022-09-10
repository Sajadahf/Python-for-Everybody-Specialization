import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

current_repeat_count = 0
url = input("Enter - ")
repeat_count = int(input("Enter count: "))
position = int(input("Enter position: "))

def parsehtml(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print("Retrieving: ", url)
    tags = parsehtml(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print("Last_Url: ", url)
