import re
data = "From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("\S+?@\S+", data)
print(y)
