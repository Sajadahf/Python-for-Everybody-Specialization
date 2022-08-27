import re

# Non-Greedy Matching
x = "From: Using the : Charecting"
y = re.findall("^F.+?:", x)
print(y)
