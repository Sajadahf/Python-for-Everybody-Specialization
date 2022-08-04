# Find bigcount & bigword in a text
name = input('Enter file name: ')
text = open(name)

counts = dict()
for line in text:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
