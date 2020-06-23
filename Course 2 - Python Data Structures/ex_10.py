name = input("Enter file:")
if len(name) < 1 : name = "clown.txt"
hand = open(name)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v, k in tmp[:10]:
    print(k, v)
