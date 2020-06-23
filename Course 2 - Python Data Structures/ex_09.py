fname = input("Enter File: ")
if len(fname) < 1:
    fname = "clown.txt"
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        ## Look up the old count for word w.  If you don't see it, use 0.
        #oldcount = di.get(w, 0)
        ## Display what the old count is.
        #print(w, "old", oldcount)
        ## Increment the count by 1.
        #newcount = oldcount + 1
        ## Set the new count equal to 1 + the old count.
        #di[w] = newcount

        ## This line replaces the previous 4 commmands.
        ## Idiom: Retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

## Now we find the most common word.
largest = -1
theword = None
## di.items() says give me all key and value items within di.
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k
print(theword, largest)
