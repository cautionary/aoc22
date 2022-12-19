infile = open('d01i01.txt', 'r')

lines = infile.readlines()

calorie_counts = []

current_calories = 0
for line in lines:
    line = line.strip()
    if line != '':
        current_calories = current_calories + int(line)
    else:
        calorie_counts.append(current_calories)
        current_calories = 0

calorie_counts.sort(reverse=True)
print(calorie_counts[0] + calorie_counts[1] + calorie_counts[2])
