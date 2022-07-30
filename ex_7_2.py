f_name = input('Enter the file name: ')
h_name = open(f_name)
f_sm = 0.0000
f_num = 0.0000
count = 0
average = 0.00000000000000000
for line in h_name:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    f_num = float(line[21:])
    f_sm = f_sm + f_num
average = f_sm / count
print('Average spam confidence:', average)
