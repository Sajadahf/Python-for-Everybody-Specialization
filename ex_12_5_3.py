import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

countos = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    countos += 1
print('Count ', countos)
print('Sum ', sum)
