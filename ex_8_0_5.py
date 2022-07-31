numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    finp = float(inp)
    numlist.append(finp)
average = sum(numlist) / len(numlist)
print('Average:', average)
