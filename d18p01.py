f =  open('d18i01.txt','r')
lines = f.readlines()

coordsets = []
for line in lines:
    numstrs = line.strip().split(',')
    coords = (int(numstrs[0]), int(numstrs[1]), int(numstrs[2]))
    coordsets.append(coords)

pairs = set()

for a in coordsets:
    for b in coordsets:
        if a != b:
            if a[0] == b[0] and a[1] == b[1] and abs(a[2] - b[2]) == 1 \
              or a[0] == b[0] and a[2] == b[2] and abs(a[1] - b[1]) == 1 \
              or a[2] == b[2] and a[1] == b[1] and abs(a[0] - b[0]) == 1: 
                    pairs.add((min(a, b), max(a,b)))

answer = ((len(coordsets) * 6) - (len(pairs) * 2))
print(answer)
