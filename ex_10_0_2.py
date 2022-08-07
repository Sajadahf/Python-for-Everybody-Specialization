d = {'a': 10, 'd': 12, 'b': 8, 'c': 9}
#print(d.items())

#print('Sorted by Key:', sorted(d.items()))

#for k,v in sorted(d.items()):
    #print(k,v)

tmp = list()
for k,v in d.items():
    tmp.append( (v,k) )
print(tmp)


print('Sorted by Key:', sorted(d.items()))
tmp = sorted(tmp, reverse=True)
print('Sorted by Value', tmp)
