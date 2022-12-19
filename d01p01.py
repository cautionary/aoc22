infile = open('d01i01.txt', 'r')

lines = infile.readlines()


max_calories = 0
current_calories = 0
for line in lines:
    line = line.strip()
    if line != '':
        current_calories = current_calories + int(line)
    else:
        max_calories = max(current_calories, max_calories)
        current_calories = 0

print(max_calories)
