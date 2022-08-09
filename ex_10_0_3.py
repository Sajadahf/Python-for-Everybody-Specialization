fhand = open("mbox-short.txt")
counts = dict()

for line in fhand:
    line.rstrip()
    words = line.split()
    for wrd in words:
        counts[wrd] = counts.get(wrd, 0) + 1
#print(counts)

lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)
#print(lst)

lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(v,k)
