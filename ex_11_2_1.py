import re

# Maching & Extracting data

x ="Subject: [sakai] svn commit: r39772 - content/branches/sakai_2-5-x/content-impl/impl/src/java/12-23org/sakaiproject/content/impl"
y = re.findall("[0-9]+", x)
print(y)
y = re.findall("[AEIOU]+", x)
print(y)
