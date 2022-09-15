import urllib.request, urllib.parse, urllib.error
import json


json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = urllib.request.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
obj = json.loads(data)

sum = 0
number = 0

for comment in obj["comments"]:
    sum += int(comment["count"])
    number += 1
print('Count:', number)
print('Sum:', sum)
