fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith("From "):
        continue
    stime = words[5]
    chour = stime[0:2]
    counts[chour] = counts.get(chour, 0) + 1

lst = list()
for k,v in counts.items():
    newtup = (k,v)
    lst.append(newtup)

lst = sorted(lst)
for k,v in lst[:]:
    print(k,v)
