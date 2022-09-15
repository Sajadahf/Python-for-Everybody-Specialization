import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = address = input('Enter location: ')
sum = 0
number = 0
print('Retrieving', address)
xml = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(xml), 'characters')
tree = ET.fromstring(xml)
counts = tree.findall('comments/comment')

for count in counts:
    sum += int(count.find("count").text)
    number += 1
print("Count:", number)
print("Sum:",sum)
