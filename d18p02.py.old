f =  open('d18i01.txt','r')
lines = f.readlines()

maxnum = 0

def check_coords(x, y, z):
    coord = (x, y, z-1)
    if coord in coordsets:
        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
    else:
        coord2 = (x, y, z-2) 
        if coord2 in coordsets:
            surface_faces.add((min(coord, coord2), max(coord, coord2)))
        else:
            for coord3 in [(x, y, z-3),
                             (x, y+1, z-2),
                             (x, y-1, z-2),
                             (x+1, y, z-2),
                             (x-1, y, z-2)]:
                if coord3 in coordsets:
                    surface_faces.add((min(coord2, coord3), max(coord2, coord3)))
    coord = (x, y, z+1)
    if coord in coordsets:
        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
    else:
        coord2 = (x, y, z+2) 
        if coord2 in coordsets:
            surface_faces.add((min(coord, coord2), max(coord, coord2)))
        else:
            for coord3 in [(x, y, z+3),
                             (x, y+1, z+2),
                             (x, y-1, z+2),
                             (x+1, y, z+2),
                             (x-1, y, z+2)]:
                if coord3 in coordsets:
                    surface_faces.add((min(coord2, coord3), max(coord2, coord3)))
    coord = (x, y-1, z)
    if coord in coordsets:
        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
    else:
        coord2 = (x, y-2, z) 
        if coord2 in coordsets:
            surface_faces.add((min(coord, coord2), max(coord, coord2)))
        else:
            for coord3 in [(x, y-3, z),
                             (x, y-2, z-1),
                             (x, y-2, z+1),
                             (x+1, y-2, z),
                             (x-1, y-2, z)]:
                if coord3 in coordsets:
                    surface_faces.add((min(coord2, coord3), max(coord2, coord3)))
    coord = (x, y+1, z)
    if coord in coordsets:
        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
    else:
        coord2 = (x, y+2, z) 
        if coord2 in coordsets:
            surface_faces.add((min(coord, coord2), max(coord, coord2)))
        else:
            for coord3 in [(x, y+3, z),
                             (x, y+2, z-1),
                             (x, y+2, z+1),
                             (x+1, y+2, z),
                             (x-1, y+2, z)]:
                if coord3 in coordsets:
                    surface_faces.add((min(coord2, coord3), max(coord2, coord3)))
    coord = (x-1, y, z)
    if coord in coordsets:
        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
    else:
        coord2 = (x-2, y, z) 
        if coord2 in coordsets:
            surface_faces.add((min(coord, coord2), max(coord, coord2)))
        else:
            for coord3 in [(x-3, y, z),
                             (x-2, y, z-1),
                             (x-2, y, z+1),
                             (x-2, y-1, z),
                             (x-2, y+1, z)]:
                if coord3 in coordsets:
                    surface_faces.add((min(coord2, coord3), max(coord2, coord3)))
    coord = (x+1, y, z)
    if coord in coordsets:
        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
    else:
        coord2 = (x+2, y, z) 
        if coord2 in coordsets:
            surface_faces.add((min(coord, coord2), max(coord, coord2)))
        else:
            for coord3 in [(x+3, y, z),
                             (x+2, y, z-1),
                             (x+2, y, z+1),
                             (x+2, y-1, z),
                             (x+2, y+1, z)]:
                if coord3 in coordsets:
                    surface_faces.add((min(coord2, coord3), max(coord2, coord3)))


coordsets = set()
for line in lines:
    numstrs = line.strip().split(',')
    coords = (int(numstrs[0]), int(numstrs[1]), int(numstrs[2]))
    maxnum = max(maxnum, coords[0], coords[1], coords[2])
    coordsets.add(coords)

maxnum += 1
    
xbcols = []
xtcols = []
for x in range(maxnum):
    xbcols.append([])
    xtcols.append([])
    for y in range(maxnum):
        xbcols[x].append(maxnum)
        xtcols[x].append(-1)
        for z in range(maxnum):
            if (x, y, z) in coordsets:
                xbcols[x][y] = min(xbcols[x][y], z)
                xtcols[x][y] = max(xtcols[x][y], z)

ybcols = []
ytcols = []
for x in range(maxnum):
    ybcols.append([])
    ytcols.append([])
    for z in range(maxnum):
        ybcols[x].append(maxnum)
        ytcols[x].append(-1)
        for y in range(maxnum):
            if (x, y, z) in coordsets:
                ybcols[x][z] = min(ybcols[x][z], y)
                ytcols[x][z] = max(ytcols[x][z], y)

zbcols = []
ztcols = []
for y in range(maxnum):
    zbcols.append([])
    ztcols.append([])
    for z in range(maxnum):
        zbcols[y].append(maxnum)
        ztcols[y].append(-1)
        for x in range(maxnum):
            if (x, y, z) in coordsets:
                zbcols[y][z] = min(zbcols[y][z], x)
                ztcols[y][z] = max(ztcols[y][z], x)
surface_faces = set()

for x in range(maxnum):
    for y in range(maxnum):
        if xbcols[x][y] < maxnum:
            for z in range(xbcols[x][y]):
                check_coords(x, y, z)
#                for coord in [(x, y, z-1),
#                              (x, y, z+1),
#                              (x, y-1, z),
#                              (x, y+1, z),
#                              (x-1, y, z),
#                              (x+1, y, z)]:
#                    if coord in coordsets:
#                        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
        if xtcols[x][y] >= 0:
            for z in range(maxnum, xtcols[x][y], -1):
                check_coords(x, y, z)
#                for coord in [(x, y, z-1),
#                              (x, y, z+1),
#                              (x, y-1, z),
#                              (x, y+1, z),
#                              (x-1, y, z),
#                              (x+1, y, z)]:
#                    if coord in coordsets:
#                        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
for x in range(maxnum):
    for z in range(maxnum):
        if ybcols[x][z] < maxnum:
            for y in range(ybcols[x][z]):
                check_coords(x, y, z)
#                for coord in [(x, y, z-1),
#                              (x, y, z+1),
#                              (x, y-1, z),
#                              (x, y+1, z),
#                              (x-1, y, z),
#                              (x+1, y, z)]:
#                    if coord in coordsets:
#                        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
        if ytcols[x][z] >= 0:
            for y in range(maxnum, ytcols[x][z], -1):
                check_coords(x, y, z)
#                for coord in [(x, y, z-1),
#                              (x, y, z+1),
#                              (x, y-1, z),
#                              (x, y+1, z),
#                              (x-1, y, z),
#                              (x+1, y, z)]:
for y in range(maxnum):
    for z in range(maxnum):
        if zbcols[y][z] < maxnum:
            for x in range(zbcols[y][z]):
                check_coords(x, y, z)
#                for coord in [(x, y, z-1),
#                              (x, y, z+1),
#                              (x, y-1, z),
#                              (x, y+1, z),
#                              (x-1, y, z),
#                              (x+1, y, z)]:
        if ztcols[y][z] >= 0:
            for x in range(maxnum, ztcols[y][z], -1):
                check_coords(x, y, z)
#                for coord in [(x, y, z-1),
#                              (x, y, z+1),
#                              (x, y-1, z),
#                              (x, y+1, z),
#                              (x-1, y, z),
#                              (x+1, y, z)]:
#                    if coord in coordsets:
#                        surface_faces.add((min((x,y,z), coord), max((x,y,z), coord)))
print(len(surface_faces))

#for pair in surface_faces:
#    print(pair)

#4126 too high
#3006 too high

#2487 too low
#2489 wrong
#2490 wrong; someone else's answer
#2494 wrong but someone else's answer
#2663 wrong
