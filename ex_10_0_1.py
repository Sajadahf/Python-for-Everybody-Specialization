# Tuples & Dictionaries
d = dict()
d['csxe'] = 2
d['zxsa'] = 5
for k,v in d.items():
    print(k, v)

tups = d.items()
print(tups)

# Tuples are Comparable
if (1, 2 , 3) < (2, 3, 4):
    print('True')
else:
    print('False')

if (1, 2 , 20000) < (1, 3, 4):
    print('True')
else:
    print('False')

if ('Junes', 'David') < ('Junes', 'Sam'):
    print('True')
else:
    print('False')

if ('Junes', 'David') > ('Juxes', 'Sam'):
    print('True')
else:
    print('False')
