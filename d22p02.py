f = open("d22i01.txt")
inp = f.read()

board_lines, path_line = inp.split("\n\n")

path_line = path_line.strip()

tiles = set()
walls = set()
rows = {}
cols = {}

r = 1
for row in board_lines.split("\n"):
    c = 1
    rstart = 10000
    rend = 0
    for col in row:
        if c not in cols:
            cols[c] = (10000, 0)
        if col == ".":
            tiles.add(complex(c, r))
            rstart = min(rstart, c)
            rend = max(rend, c)
            cols[c] = ((min(cols[c][0], r), max(cols[c][1], r)))
        elif col == "#":
            walls.add(complex(c, r))
            rstart = min(rstart, c)
            rend = max(rend, c)
            cols[c] = ((min(cols[c][0], r), max(cols[c][1], r)))
        c += 1
    rows[r] = (rstart, rend)
    r+= 1

num = ""
instructions = []
p = 0
while p < len(path_line):
    if path_line[p].isnumeric():
        num += path_line[p]
    else:
        instructions.append(int(num))
        num = ""
        instructions.append(path_line[p])
    p += 1
instructions.append(int(num))

facing = 0
move_ops = [1 + 0j, 1j, -1 + 0j, -1j]
pos = complex(rows[1][0], 1)

for instr in instructions:
    if isinstance(instr, int):
        for i in range(instr):
            next_pos = pos + move_ops[facing]
            if next_pos not in walls and next_pos not in tiles:
                if facing == 0:
                    if pos.imag < 51: #f
                        next_pos = complex(100, 151 - pos.imag)
                        if next_pos in tiles:
                            facing = 2
                    elif pos.imag < 101: #g
                        next_pos = complex(pos.imag + 50, 50)
                        if next_pos in tiles:
                            facing = 3
                    elif pos.imag < 151: #f
                        next_pos = complex(150, 151 - pos.imag)
                        if next_pos in tiles:
                            facing = 2
                    else: #k
                        next_pos = complex(pos.imag - 100, 150)
                        if next_pos in tiles:
                            facing = 3
                elif facing == 1:
                    if pos.real < 50: #e
                        next_pos = complex(pos.real + 100, 1)
                    elif pos.real < 101: #k
                        next_pos = complex(50, pos.real + 100)
                        if next_pos in tiles:
                            facing = 2
                    else: #g
                        next_pos = complex(100, pos.real - 50)
                        if next_pos in tiles:
                            facing = 2
                elif facing == 2:
                    if pos.imag < 51: #b
                        next_pos = complex(1, 151 - pos.imag)
                        if next_pos in tiles:
                            facing = 0
                    elif pos.imag < 101: #h
                        next_pos = complex(pos.imag - 50 , 101)
                        if next_pos in tiles:
                            facing = 1
                    elif pos.imag < 151: #b
                        next_pos = complex(51, 151 - pos.imag)
                        if next_pos in tiles:
                            facing = 0
                    else: #a
                        next_pos = complex(pos.imag - 100 , 1)
                        if next_pos in tiles:
                            facing = 1
                elif facing == 3:
                    if pos.real < 51: #h
                        next_pos = complex(51, pos.real + 50)
                        if next_pos in tiles:
                            facing = 0
                    elif pos.real < 101: #a
                        next_pos = complex(1, pos.real + 100)
                        if next_pos in tiles:
                            facing = 0
                    else: #e
                        next_pos = complex(pos.real - 100 , 200)
            if next_pos in tiles:
                pos = next_pos
    elif instr == 'R':
        facing = (facing + 1) % 4
    elif instr == 'L':
        facing = (facing - 1) % 4

answer = int(pos.imag * 1000 + pos.real * 4 + facing)
print(answer)
