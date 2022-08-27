# Extracting a host name - usinf find and string slicing
data = "From cwen@iupui.edu.ac.ir Fri Jan  4 11:35:08 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
