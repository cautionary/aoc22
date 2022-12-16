input = open('d10i01.txt', 'r')
lines = input.readlines()

cycle = 1
xreg = 1

values = [1]

for line in lines:
    line = line.strip()
    instr = line.split()[0]
    if instr == "addx":
        cycle += 1
        values.append(xreg)
        val = int(line.split()[1])
        xreg += val
        values.append(xreg)
        cycle += 1
    else:
        cycle += 1
        values.append(xreg)

answer = 0
for i in [20, 60, 100, 140, 180, 220]:
    print(values[i-1])
    answer += i * values[i-1]

print(answer)
