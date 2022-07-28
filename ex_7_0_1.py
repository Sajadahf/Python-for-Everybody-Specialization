testfile = open('Test.txt', 'r')
count = 0
for line in testfile:
    print(line)
    count = count + 1
print(f'***{count}***')
