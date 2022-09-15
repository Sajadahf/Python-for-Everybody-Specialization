import json

data = '''
{
    "name" : "Sajad",
    "phone" : {
        "type" : "intl",
        "number" : "+98 938 339 4918"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("Email:", info["email"]["hide"])
