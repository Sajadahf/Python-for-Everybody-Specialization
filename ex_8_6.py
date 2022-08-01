text = open('mbox-short.txt')

for line in text:
    line = line.rstrip()
    words = line.split()
#    print(words)
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
