fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mclown.txt'
hand = open(fname)

lib = dict()
for line in hand:
    line = line.rstrip()
    wrds = line.split()

    for w in wrds:
        if w in lib:
            lib[w] = lib[w] + 1
            print("**Existing**")
        else:
            lib[w]= 1
            print("**New**")
        print(w, lib[w])
