f =  open('d14i01.txt','r')

def find_min_rock_500(rock):
	min_height = 10000
	for r in rock:
		if r.real == 500:
			min_height = min(min_height, r.imag)
	return int(min_height)

def find_max_rock(rock):
	max_height = 0
	for r in rock:
		max_height = max(max_height, r.imag)
	return int(max_height)


lines = f.readlines()

rock = set()
for line in lines:
	points = line.strip().split(" -> ")
	for i in range(len(points)):
		if i < len(points) - 1:
			a = complex (int(points[i].split(',')[0]), int(points[i].split(',')[1]))
			b = complex (int(points[i+1].split(',')[0]), int(points[i+1].split(',')[1]))
			if a.real == b.real:
				for k in range(abs(int(a.imag - b.imag)) + 1):
					rock.add(complex(a.real, min(a.imag, b.imag) + k))
			elif a.imag == b.imag:
				for k in range(abs(int(a.real - b.real)) + 1):
					rock.add(complex(min(a.real, b.real) + k, a.imag))
		
first_sand_height = find_min_rock_500(rock)
floor = find_max_rock(rock) + 2

for i in range(-1000, 2000):
	rock.add(complex(i, floor))


sand = [complex(500,first_sand_height - 1)]
rock.add(complex(500,first_sand_height - 1))
done = False

c = 0
while not done:
	if c % 500 == 0:
		print(len(sand))
	c += 1
	drop_point = complex(500, find_min_rock_500(rock) - 1)
	settled = False
	while not settled:
		if (drop_point + complex(0, 1)) not in rock:
			drop_point = drop_point + complex(0,1)
		elif (drop_point + complex(-1, 1)) not in rock:
			drop_point = drop_point + complex(-1, 1)
		elif (drop_point + complex(1, 1)) not in rock:
			drop_point = drop_point + complex(1, 1)
		else:
			rock.add(drop_point)
			sand.append(drop_point)
			settled = True
	if drop_point == complex(500, 0):
		done = True
print(len(sand))
