f = open("d23i01.txt")
lines = f.readlines()

def has_neighbor(elves, elf):
    for spot in [-1 - 1j,
                 -1 + 0j, 
                 -1 + 1j, 
                 1 - 1j,  
                 1 + 0j,  
                 -1j,  
                 1j,  
                 1 + 1j]:
        if elf + spot in elves:
            return True
    return False

elves = set()
#NSWE
edges = [100, 0, 100, 0]
for r in range(len(lines)):
    line = lines[r].strip()
    for c in range(len(line)):
        if line[c] == '#':
           elves.add(complex(r, c))

directions = ['N', 'S', 'W', 'E']
checks = {'N': [-1 - 1j, -1 + 0j, -1 + 1j],
          'S': [ 1 - 1j,  1 + 0j,  1 + 1j],
          'W': [-1 - 1j,     -1j,  1 - 1j],
          'E': [-1 + 1j,      1j,  1 + 1j]}

moves = {'N': -1 + 0j,
         'S': 1 + 0j,
         'W': -1j,
         'E': 1j}

for i in range(10):
    proposals = {}
    for elf in elves:
        if has_neighbor(elves, elf):
            move_proposed = False
            for dir in directions:
                if not move_proposed:
                    conflict = False
                    for check in checks[dir]:
                        if elf + check in elves:
                            conflict = True
                    if not conflict:
                        move_proposed = True
                        move = elf + moves[dir]
                        if move in proposals:
                            proposals[move] = None
                        else:
                            proposals[move] = elf

    for proposal in proposals:
        if proposals[proposal] != None:
            elves.remove(proposals[proposal])
            elves.add(proposal)
            edges[0] = int(min(edges[0], proposal.real))
            edges[1] = int(max(edges[1], proposal.real))
            edges[2] = int(min(edges[2], proposal.imag))
            edges[3] = int(max(edges[3], proposal.imag))


    directions.append(directions.pop(0))

area = (abs(edges[0] - edges[1]) + 1) * (abs(edges[2] - edges[3]) + 1)
answer = area - len(elves)
print(answer)

#print(" ", end="")
#for c in range(edges[2], edges[3] + 1):
#    d = c % 10
#    print("%s" % d, end="")
#print()
#for r in range(edges[0], edges[1] + 1):
#    print(r % 10, end="")
#    for c in range(edges[2], edges[3] + 1):
#        if complex(r, c) in elves:
#            print('#', end="")
#        else:
#            print('.', end="")
#    print()

