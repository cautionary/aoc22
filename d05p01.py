import re


f =  open('d05i01.txt','r')

lines = f.readlines()


stacks = [None, [], [], [], [], [], [], [], [], []]
rules = []
section = "stacks"

#[J] [S] [N] [R] [M] [T] [G] [C] [D]
#move 1 from 8 to 4

for line in lines:
	line = line.strip()
	if line == "":
		section = "steps"
	if section == "stacks":
		matches = re.match("(\[\w\]|   )? (\[\w\]|   )? (\[\w\]|   )? (\[\w\]|   )? (\[\w\]|   )? (\[\w\]|   )? (\[\w\]|   )? (\[\w\]|   )? (\[\w\])?", line)
		if matches:
			for i in range(1, 10):
				if matches[i] != "   ":
					stacks[i].insert(0,matches[i][1])

	if section == "steps":
		matches = re.match("move (\d+) from (\d+) to (\d+)", line)
		if matches:
			rules.append({'quant': int(matches[1]), 
					'from': int(matches[2]), 
					'to': int(matches[3])})


for rule in rules:
	for i in range(rule['quant']):
		crate = stacks[rule['from']].pop()
		stacks[rule['to']].append(crate)

for i in range(1,10):
	print(stacks[i][-1], end='')

print()		
