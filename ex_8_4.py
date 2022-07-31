romeo = open('romeo.txt', 'r')
listt = list()
listtt = list()
for line in romeo:
    line = line.rstrip()
    words = line.split()
    listt = listt + words

for i in range(len(listt)):
    onebyone = listt[i]
    if not onebyone in listtt:
        listtt.append(onebyone)

listtt.sort()
print(listtt)
