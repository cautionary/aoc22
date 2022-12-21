f = open("d21i01.txt")
lines = f.readlines()


def trav_monkeys(monkeys, monkey):
    phrase = monkeys[monkey]
    if isinstance(phrase, int):
        return phrase
    else:
        if phrase[1] == '+':
            return trav_monkeys(monkeys, phrase[0]) + trav_monkeys(monkeys, phrase[2])
        elif phrase[1] == '-':
            return trav_monkeys(monkeys, phrase[0]) - trav_monkeys(monkeys, phrase[2])
        elif phrase[1] == '*':
            return trav_monkeys(monkeys, phrase[0]) * trav_monkeys(monkeys, phrase[2])
        elif phrase[1] == '/':
            return trav_monkeys(monkeys, phrase[0]) // trav_monkeys(monkeys, phrase[2])
        elif phrase[1] == '=':
            return (trav_monkeys(monkeys, phrase[0]), trav_monkeys(monkeys, phrase[2]))


monkeys = {}
for line in lines:
    monkey, phrase = line.strip().split(': ')
    if len(phrase) < 3:
        monkeys[monkey] = int(phrase)
    else:
        monkeys[monkey] = phrase.split()
monkeys["root"] = (monkeys["root"][0], "=", monkeys["root"][2])

found = False
#for i in range(3429411069020, 3429411069030, 1):
#    monkeys["humn"] = i
#    res = trav_monkeys(monkeys, "root")
#    print(i, res, res[0] - res[1])
i = 1
mag = 0
while not found:
    monkeys["humn"] = 10 ** i
    res = trav_monkeys(monkeys, "root")
    if res[0] - res[1] < 0:
        mag = i - 1
        found = True
    i += 1
found = False
num = 10 ** mag
3429411069020
digits = []
while not found:
    for i in range(11):
        num = 0
        for digit, power in digits:
            num += digit * 10 ** power
        num = num + 10 ** mag * i
        monkeys["humn"] = num
        res = trav_monkeys(monkeys, "root")
        if res[0] - res[1] == 0:
            print(num)
            found = True
            break
        if res[0] - res[1] < 0:
            digits.append((i-1, mag))
            mag -= 1
            break
        



