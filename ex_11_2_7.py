import re

# The Regex Version
lin = "From cwen@iupui.edu.ac.ir Fri Jan  4 11:35:08 2008"
y = re.findall("@([^ ]*)", lin)
print(y)

# Even Cooler Regex Version
y = re.findall("^From .*@([^ ]+)", lin)
print(y)
