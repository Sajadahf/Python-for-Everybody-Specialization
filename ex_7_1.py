f_name = input('Enter the file name: ')
h_name = open(f_name)

for line in h_name:
    line = line.upper().rstrip()
    print(line)
