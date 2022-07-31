total = 0
count = 0
while True:
    num = input('Enter a number: ')
    if num == 'done': break
    fnum = float(num)
    total = fnum + total
    count += 1
average = total / count
print('Average: ', average)    
