import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Sajad</name>
    <phone type = "intl">
        +98 938 339 4918
    </phone>
    <email hide = "Yes"/>
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Email:", tree.find("email").get("hide"))
