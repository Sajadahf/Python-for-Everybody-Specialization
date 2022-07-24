num = 0
tot = 0.0
while True:
    try:
        sval = input('Enter a number: ')
        if sval == 'done' and tot == 0:
            print("Enter a valid input")
            continue
        if sval == 'done' and tot != 0:
            break
        fval = float(sval)
        num = num + 1
        tot = tot + fval

    except:
        print('Invalid Input')
        continue

print(tot, num, tot / num)
