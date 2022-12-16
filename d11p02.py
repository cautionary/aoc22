import re

input = open('d11i01.txt', 'r')
lines = input.read()

monkeys = []

monkeys_text = lines.split("\n\n")

for monkey_text in monkeys_text:
    monkey = {}
    lines = monkey_text.split("\n")
    start_items = lines[1].split(": ")[1].split(",")
    monkey['items'] = []
    for start_item in start_items:
        monkey['items'].append(int(start_item))

    operation_matches = re.match("  Operation: new = old (.) (old|\d+)", lines[2])
    operation = operation_matches[1]
    op_value = operation_matches[2]

    if op_value == "old":
        operation = "**"
        op_value = 2

    monkey['operation'] = (operation, int(op_value))

    monkey['test'] = int(re.match("  Test: divisible by (\d+)", lines[3])[1])
    
    monkey['test_true'] = int(re.match("    If true: throw to monkey (\d+)", lines[4])[1])
    monkey['test_false'] = int(re.match("    If false: throw to monkey (\d+)", lines[5])[1])

    monkey['inspections'] = 0

    monkeys.append(monkey) 

prod_of_tests = 1
for monkey in monkeys:
    prod_of_tests = prod_of_tests * monkey['test']

for i in range(10000):
    for m in range(len(monkeys)):
        op = monkeys[m]['operation']
        test = monkeys[m]['test']
        dest_t = monkeys[m]['test_true']
        dest_f = monkeys[m]['test_false']
        for item in monkeys[m]['items']:
            monkeys[m]['inspections'] += 1
            if op[0] == "*":
                item = item * op[1]
            elif op[0] == "**":
                item = item ** op[1]
            elif op[0] == "+":
                item = item + op[1]
            
            item = item % prod_of_tests

            if item % test == 0:
                monkeys[dest_t]['items'].append(item)
            else:
                monkeys[dest_f]['items'].append(item)
        monkeys[m]['items'] = []

inspections = []
for monkey in monkeys:
    inspections.append(monkey['inspections'])

inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
