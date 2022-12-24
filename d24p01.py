f = open("d24i01.txt")
lines = f.readlines()

start = complex(0, lines[0].index('.'))
end = complex(len(lines) - 1, lines[-1].index('.'))

blizzes = {'>': set(), '<': set(), '^': set(), 'v': set()}
move_ops = {'>': 1j, 'v': 1 + 0j, '^': -1 + 0j, '<': -1j}

for i in range(1, len(lines) - 1):
    for k in range(1, len(lines[i].strip()) -1):
        if lines[i][k] != '.':
            blizzes[lines[i][k]].add(complex(i, k))

def print_map():
    print(" ", end="")
    for c in range(len(lines[0].strip())):
        print(c % 10, end="")
    print()
    for r in range(len(lines)):
        print(r % 10, end="")
        for c in range(len(lines[0].strip())):
            if complex(r, c) == pos:
                print("E", end="")
            elif r == 0 or r == len(lines) - 1:
                if complex(r, c) == start \
                  or complex(r, c) == end:
                    print(".", end="")
                else:
                    print("#", end="")
            elif c == 0 or c == end.imag + 1:
                print("#", end="")
            else:
                bliz_found = []
                for d in ['<', '>', '^', 'v']:
                    if complex(r, c) in blizzes[d]:
                        bliz_found.append(d)
                if len(bliz_found) == 0:
                    print(' ', end="")
                elif len(bliz_found) == 1:
                    print(bliz_found[0], end="")
                else:
                    print(len(bliz_found), end="")
        print()

def move_bliz(blizzes):
    new_blizzes = {'>': set(), '<': set(), '^': set(), 'v': set()}
    for d in move_ops:
        for bliz in blizzes[d]:
            bliz = bliz + move_ops[d]
            if bliz.imag < 1:
                bliz = complex(bliz.real, end.imag)
            elif bliz.imag > end.imag:
                bliz = complex(bliz.real, 1)
            elif bliz.real < 1:
                bliz = complex(end.real -1, bliz.imag)
            elif bliz.real == end.real:
                bliz = complex(1, bliz.imag)
            new_blizzes[d].add(bliz)
    return new_blizzes

def open_neighbors(blizzes, pos):
    open_spots = []
    for dir in move_ops:
        spot = pos + move_ops[dir]
        if spot == end \
                or (spot.real > 0 and spot.real < end.real \
                and spot.imag > 0 and spot.imag <= end.imag):
            found = False
            for d2 in move_ops:
                if spot in blizzes[d2]:
                    found = True
            if not found:
                open_spots.append(spot)
    found = False
    for d2 in move_ops:
        if pos in blizzes[d2]:
            found = True
    if not found:
        open_spots.append(pos)
    return open_spots

def revert_save():
    global c
    global pos
    global saves
    global blizzes
    global win
    if len(saves) > 0:
        save = [10001, 0, 0, 0]

        while save[0] > win:
            if (save[0], save[3]) in done_saves:
                save = saves.pop()
            else:
                save = saves.pop()
                done_saves.add((save[0], save[3]))
        c = save[0]
        blizzes = save[1]
        pos = save[2][0]
        if len(save[2]) > 1:
            saves.append((c, blizzes, save[2][1:], pos))
        else:
            done_saves.add((c, pos)) 

saves = []
done_saves = set()
done = False
pos = start
win = 10000
c = 0
while not done:
    print(c, win, len(saves), len(done_saves))
    for save in saves:
        if save[0] >= win:
            saves.remove(save)
            done_saves.add((save[0], save[3]))
        elif (save[0], save[3]) in done_saves:
            saves.remove(save)
    if pos == end:
        win = min(win, c)
        if len(saves) > 0:
            revert_save()
        else:
            print(win)
            done = True
            exit()
    if c > win:
        revert_save()
    #print_map()
    #print()
    c += 1
    blizzes = move_bliz(blizzes)
    opens = open_neighbors(blizzes, pos)
    if len(opens) == 1:
        pos = opens[0]
    elif len(opens) > 1:
        if (c, pos) in done_saves:
            revert_save()
        else:
            saves.append((c, blizzes, opens[1:], pos))
            pos = opens[0]
    elif len(opens) == 0:
        revert_save()

