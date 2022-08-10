fhand = open("romeo.txt")
counts = dict()

for line in fhand:
    line.rstrip()
    words = line.split()
    for wrd in words:
        counts[wrd] = counts.get(wrd, 0) + 1

print(sorted( [(v,k) for k,v in counts.items()], reverse=True))
