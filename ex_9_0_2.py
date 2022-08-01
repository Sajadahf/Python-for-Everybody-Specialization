# Add new names
counts = dict()
names = ['csew', 'csew', 'dsaz', 'csew', 'dsaz', 'wsxz']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
