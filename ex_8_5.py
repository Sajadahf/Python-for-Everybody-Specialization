text_in = open('mbox-short.txt', 'r')
count = 0
for line in text_in:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From '): continue
    print(words[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
