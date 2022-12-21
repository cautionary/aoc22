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


monkeys = {}
for line in lines:
    monkey, phrase = line.strip().split(': ')
    if len(phrase) < 3:
        monkeys[monkey] = int(phrase)
    else:
        monkeys[monkey] = phrase.split()

print(trav_monkeys(monkeys, "root"))
