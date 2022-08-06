fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mclown.txt'
hand = open(fname)

lib = dict()
for line in hand:
    line = line.rstrip()
    wrds = line.split()

    for w in wrds:
        # idioms: retrieve/create/update counter
        lib[w] = lib.get(w, 0) + 1

#print(lib)

# Now we want to find the most common word
largest = -1
theword = None
for key,val in lib.items() :
    #print(key, val)
    if val > largest :
        largest = val
        theword = key
print("Done ----->", theword, largest)
