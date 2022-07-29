f_name = input('Enter the file name: ')
h_name = open(f_name)
f_sum = 0.0000
f_num = 0.0000
count = 0
average = 0.00000000000000000
for line in h_name:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    f_num = float(line[21:])
    f_sum = f_sum + f_num
average = f_sum / count
print('Average spam confidence:', average)
