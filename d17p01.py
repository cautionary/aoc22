f =  open('d17i01.txt','r')
lines = f.read()

jets = lines.strip()

#jets = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

TWIDTH = 7
RSTARTX = 2
RSTARTY = 3
rtype = ['-', '+', 'L', '|', 'o']
rocks = {'-': [[1,1,1,1]],
         '+': [[0,1,0],[1,1,1],[0,1,0]],
         'L': [[0,0,1],[0,0,1],[1,1,1]],
         '|': [[1],[1],[1],[1]],
         'o': [[1,1],[1,1]]}

tunnel_spots = {0j,1j,2j,3j,4j,5j,6j}
tunnel_max = 0

def collision(tspots, rock, rpos, direc):
    rheight = len(rock)
    rwidth = len(rock[0])
    rock_spots = []
    if direc == "right" and pos.imag + rwidth >= TWIDTH:
        return True
    if direc == "left" and pos.imag == 0:
        return True
    
    for r in range(rheight - 1, -1, -1):
        for c in range(rwidth):
            if rock[r][c] == 1:
                rock_spots.append(rpos + complex(rheight - r - 1, c))

    for rs in rock_spots:
        if direc == "down":
            check = rs - (1 + 0j)
        elif direc == "left":
            check = rs - 1j
        elif direc == "right":
            check = rs + 1j
        if check in tunnel_spots:
            return True
    return False
    
j = 0
for i in range(2022):
    rock = rocks[rtype[i % 5]]
    rheight = len(rock)
    rwidth = len(rock[0])
    pos = complex(tunnel_max + 4, 2)
    falling = True
    while falling:
        jet = jets[j % len(jets)]

        if jet == ">":
            if not collision(tunnel_spots, rock, pos, "right"):
                pos = pos + 1j
        elif jet == "<":
            if not collision(tunnel_spots, rock, pos, "left"):
                pos = pos - 1j
        if collision(tunnel_spots, rock, pos, "down"):
            for r in range(rheight - 1, -1, -1):
                tunnel_max = max(tunnel_max, int(pos.real) + rheight - 1)
                for c in range(rwidth):
                    if rock[r][c] == 1:
                        rspot = pos + complex(rheight - r - 1, c)
                        tunnel_spots.add(rspot)
            falling = False
        else:
            pos = pos + (-1 + 0j)
        j += 1

print(tunnel_max)

