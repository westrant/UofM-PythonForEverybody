# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
	print("File couldn’t be opened:", fname)
	quit()

count = 0
total = float(0)

for line in fh:
    line = line.rstrip()
    if not "X-DSPAM-Confidence:" in line:
        continue
    atpos = line.find(":")
    fval = float(line[atpos+2:])
    count = count + 1
    total = total + fval

print("Average spam confidence:", (total / count))
