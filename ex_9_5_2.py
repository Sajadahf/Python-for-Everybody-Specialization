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
        #print(w, 'New', lib[w])
print(lib)

"""
# Above code equal below code
    for w in wrds:
        # If the key not there, the count is zero
        oldcount = lib.get(w, 0)
        print(w, 'Old', oldcount)
        newcount = oldcount + 1
        lib[w] = newcount
        print(w, 'New', newcount)
"""
