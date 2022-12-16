input = open('d10i01.txt', 'r')
lines = input.readlines()

cycle = 1
xreg = 1

values = [1]

crt = ['#']

def pixel_on(cycle, xreg):
    if cycle % 40 in range(xreg - 1, xreg + 2):
        crt.append('#')
    else:
        crt.append('.')

for line in lines:
    line = line.strip()
    instr = line.split()[0]
    if instr == "addx":
        pixel_on(cycle, xreg)
        cycle += 1
        values.append(xreg)
        val = int(line.split()[1])
        xreg += val
        values.append(xreg)
        pixel_on(cycle, xreg)
        cycle += 1
    else:
        pixel_on(cycle, xreg)
        cycle += 1
        values.append(xreg)

for i in range(len(crt)):
    if i % 40 == 0:
        print('')
    print(crt[i], end="")

print()
