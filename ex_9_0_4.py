counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('words:', words)

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('countig...')
print('counts:', counts)
