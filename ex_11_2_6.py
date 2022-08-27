# The Double Split Pattern
data = "From cwen@iupui.edu.ac.ir Fri Jan  4 11:35:08 2008"
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
