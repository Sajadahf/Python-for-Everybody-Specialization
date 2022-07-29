f_name = input("Enter the file name: ")
try:
    h_file = open(f_name)

except:
    print('File not be opened:', f_name)
    quit()

count = 0
for line in h_file:
    if line.startswith('Address'):
        count += 1
print('There were', count, 'subject lines in', f_name)
