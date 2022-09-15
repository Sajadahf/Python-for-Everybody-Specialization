import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x = '3'>
            <id>001</id>
            <name>Sajad</name>
        </user>
        <user x = '6'>
            <id>009</id>
            <name>Emad</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print("User count:", len(lst))

for item in lst:
    print("Name:", item.find("name").text)
    print("Id:", item.find("id").text)
    print("Atribute:", item.get('x'))
