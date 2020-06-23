# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
	print("File couldn’t be opened:", fname)
	quit()

for line in fh:
    stripline = line.rstrip()
    print(stripline.upper())
