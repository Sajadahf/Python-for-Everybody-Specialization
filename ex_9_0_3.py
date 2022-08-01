counts = dict()
names = ['csew', 'csew', 'dsaz', 'csew', 'dsaz', 'wsxz']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
