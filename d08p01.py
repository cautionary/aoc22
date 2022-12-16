input = open('d08i01.txt', 'r')
lines = input.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

width = len(lines[0])
height = len(lines)

count = width * 2 + (height - 2) * 2

counted_trees = []

for i in range(1, len(lines)-1):
    cur_max = int(lines[i][0])
    for j in range(1, len(lines[i])-1):
        if int(lines[i][j]) > cur_max:
            if (i,j) not in counted_trees:
                count += 1
                counted_trees.append((i,j))
            cur_max = int(lines[i][j])

    cur_max = int(lines[i][-1])
    for j in range(len(lines[i])-2, 0, -1):
        if int(lines[i][j]) > cur_max:
            if (i,j) not in counted_trees:
                count += 1
                counted_trees.append((i,j))
            cur_max = int(lines[i][j])

for j in range(1, len(lines[0])-1):
    cur_max = int(lines[0][j])
    for i in range(1, len(lines)-1):
        if int(lines[i][j]) > cur_max:
            if (i,j) not in counted_trees:
                count += 1
                counted_trees.append((i,j))
            cur_max = int(lines[i][j])

    cur_max = int(lines[-1][j])
    for i in range(len(lines)-2, 0, -1):
        if int(lines[i][j]) > cur_max:
            if (i,j) not in counted_trees:
                count += 1
                counted_trees.append((i,j))
            cur_max = int(lines[i][j])

print(count)
