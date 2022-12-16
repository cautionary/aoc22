import re

f =  open('d07i01.txt','r')

lines = f.readlines()

cur_dir = []
dir_sizes = {}

def path_to_string(plist):
	working_string = ""
	for dir in plist:
		working_string += dir
		working_string += "/"
	return(working_string)

for line in lines:
	line = line.strip()
	cmd = line.split()
	if cmd[0] == '$':
		if cmd[1] == 'cd':
			if cmd[2] == '..':
				cur_dir.pop()
			else:
				cur_dir.append(cmd[2])
	elif cmd[0][0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		size = int(cmd[0])
		if path_to_string(cur_dir) in dir_sizes:
			dir_sizes[path_to_string(cur_dir)] += size
		else:
			dir_sizes[path_to_string(cur_dir)] = size
	
		for i in range(1, len(cur_dir)):
			if path_to_string(cur_dir[0:i*-1]) in dir_sizes:
				dir_sizes[path_to_string(cur_dir[0:i*-1])] += size
			else:
				dir_sizes[path_to_string(cur_dir[0:i*-1])] = size

total = 0
for dir_name in dir_sizes:
	if dir_sizes[dir_name] <= 100000:
		total += dir_sizes[dir_name]

print(total)
