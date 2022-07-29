"""
testfile = open('Test.txt', 'r')
for line in testfile:
    if line.startswith("Age"):
        print(line)
"""

""" same with above
testfile = open('Test.txt', 'r')
for line in testfile:
    if not line.startswith("Age"):
        continue
    print(line)
"""

testfile = open('Test.txt', 'r')
for line in testfile:
    if not 'Age' in line:
        continue
    print(line)
