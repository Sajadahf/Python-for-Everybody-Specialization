#name = input("Enter file name: ")
text = open('mbox-short.txt')

counts = dict()
for line in text:
    words = line.split()
    for word in words:
        if 'From' in words:
            counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        chart = word
        if chart.find('@') > 1:
            bigcount = count
            bigword = word
        else:
            continue
print(bigword, bigcount)
