import re

# Fine-Tuning String Extraction
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.findall("\S+@\S+", line):
        x = re.findall("\S+@\S+", line)
        print(x)
    if re.findall("^From (\S+@\S+)", line):
        y = re.findall("^From (\S+@\S+)", line)
        print(y)
        
