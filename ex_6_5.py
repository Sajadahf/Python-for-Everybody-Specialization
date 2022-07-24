text = "X-DSPAM-Confidence:    0.8475"

find = text.find('0')
num = text[find:find+6]
fnum = float(num)
print(fnum)
