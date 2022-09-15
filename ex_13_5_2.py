import json

input = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Sajad"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Emad"
    }
]'''

info = json.loads(input)
print("******************")
print(f"* User count: {len(info)}  *")
print("******************")
for item in info:
    print("Name:", item["name"])
    print("Id:", item["id"])
    print("Atribute:", item["x"])
    print("################")
