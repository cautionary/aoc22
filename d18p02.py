f =  open('d18i01.txt','r')
lines = f.readlines()

maxnum = 0

coordsets = set()
for line in lines:
    numstrs = line.strip().split(',')
    coords = (int(numstrs[0]), int(numstrs[1]), int(numstrs[2]))
    maxnum = max(maxnum, coords[0], coords[1], coords[2])
    coordsets.add(coords)

maxnum += 1

empties = [{(0,0,0)}]
for x in range(-1, maxnum+1):
    for y in range(-1, maxnum+1):
        for z in range(-1, maxnum+1):
            if (x, y, z) not in coordsets:
                set_found = -1
                for i in range(len(empties)):
                    if (x, y, z) in empties[i]:
                        set_found = i
                if set_found < 0:
                        empties.append({(x,y,z)})
                        set_found = len(empties) - 1
                i = set_found
                for coords in [(x,   y,   z-1),
                               (x,   y,   z+1),
                               (x,   y-1, z  ),
                               (x,   y+1, z  ),
                               (x-1, y,   z  ),
                               (x+1, y,   z  )]:
                    if coords not in coordsets:
                        empties[i].add(coords)


surface_pairs = set()

for i in range(1, len(empties)):
    merged = False
    for (x, y, z) in empties[i]:
        for coords in [(x,   y,   z+1),
                       (x,   y,   z-1),
                       (x,   y-1, z  ),
                       (x,   y+1, z  ),
                       (x-1, y,   z  ),
                       (x+1, y,   z  )]:
            if coords in empties[0]:
                empties[0] = empties[0].union(empties[i])
                empties[i] = set()
                merged = True
                break
        if merged:
            break

total_count = 0
for eset in empties:
    total_count += len(eset)
for (x, y, z) in empties[0]:
    for coords in [(x,   y,   z-1),
                   (x,   y,   z+1),
                   (x,   y-1, z  ),
                   (x,   y+1, z  ),
                   (x-1, y,   z  ),
                   (x+1, y,   z  )]:
        if coords in coordsets:
            surface_pairs.add((min((x,y,z), coords), max((x,y,z), coords)))


print(len(surface_pairs))

#4126 too high
#3006 too high

#2487 too low
#2489 wrong
#2490 wrong; someone else's answer
#2494 wrong but someone else's answer
#2497 wrong
#2663 wrong
