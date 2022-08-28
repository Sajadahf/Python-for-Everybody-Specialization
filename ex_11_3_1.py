import re

hand = open("regex_sum_1607250.txt")
sum = 0
i = 0
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall("[0-9]+", line)
    for num in stuff:
        i += 1
        sum = sum + int(num)

print("There are", i, "values with a sum=", sum)
