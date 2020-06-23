fhand = open("mbox-short.txt")
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    time = words[5].split(":")
    ## Now, let's get a count of all times.
    counts[time[0]] = counts.get(time[0], 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)
for key, val in lst:
    print(key, val)
