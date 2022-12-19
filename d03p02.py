infile = open('d03i01.txt', 'r')

lines = infile.readlines()

total = 0

rucksack_num = 0

for line in lines:
    line = line.strip()

    if rucksack_num % 3 == 0:
        for item in line:
            if item in lines[rucksack_num + 1] and item in lines[rucksack_num + 2]:
                if item.islower():
                    total += ord(item) - 96
                else:
                    total += ord(item) - 38
                break
    rucksack_num += 1

print(total)
