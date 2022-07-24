largest = None
smallest = None

while True:
    try:
        snum = input("Enter a number: ")
        if snum == 'done':
            break
        inum = int(snum)
        if smallest is None:
            smallest = inum
        elif inum < smallest:
            smallest = inum

        if largest is None:
            largest = inum
        elif inum > largest:
            largest = inum

    except:
        print('Invalid Input')
        continue

print('Maximum is', largest)
print('Minimum is', smallest)
