infile = open('d03i01.txt', 'r')

lines = infile.readlines()

total = 0

for line in lines:
    line = line.strip()

    compartment_first = line[0:(len(line)//2)]
    compartment_second = line[(len(line)//2):]

    for item in compartment_first:
        if item in compartment_second:
            if item.islower():
                total += ord(item) - 96
            else:
                total += ord(item) - 38
            break

print(total)
