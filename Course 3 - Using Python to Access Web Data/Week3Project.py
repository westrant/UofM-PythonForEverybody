import re
fhand = open("regex_sum_392834.txt")
stuff = list()
sum = 0
for line in fhand:
    y = re.findall("[0-9]+", line)
    stuff=stuff+y

for number in stuff:
    sum = sum + int(number)

print(sum)
