infile = open('d04i01.txt', 'r')

lines = infile.readlines()

count = 0

for line in lines:
    line = line.strip()

    ranges = line.split(',')
    range_e1 = ranges[0].split('-')
    range_e2 = ranges[1].split('-')

    if (
        int(range_e1[0]) in range(int(range_e2[0]), int(range_e2[1]) + 1) and 
        int(range_e1[1]) in range(int(range_e2[0]), int(range_e2[1]) + 1)
        ) or (
        int(range_e2[0]) in range(int(range_e1[0]), int(range_e1[1]) + 1) and 
        int(range_e2[1]) in range(int(range_e1[0]), int(range_e1[1]) + 1)
        ):
            count += 1

print(count)
