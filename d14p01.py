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

rock = []
for line in lines:
	points = line.strip().split(" -> ")
	for i in range(len(points)):
		if i < len(points) - 1:
			a = complex (int(points[i].split(',')[0]), int(points[i].split(',')[1]))
			b = complex (int(points[i+1].split(',')[0]), int(points[i+1].split(',')[1]))
			if a.real == b.real:
				for k in range(abs(int(a.imag - b.imag)) + 1):
					rock.append(complex(a.real, min(a.imag, b.imag) + k))
			elif a.imag == b.imag:
				for k in range(abs(int(a.real - b.real)) + 1):
					rock.append(complex(min(a.real, b.real) + k, a.imag))
		
first_sand_height = find_min_rock_500(rock)
floor = find_max_rock(rock)


sand = [complex(500,first_sand_height - 1)]
rock.append(complex(500,first_sand_height - 1))
done = False

while not done:
	drop_point = complex(500, find_min_rock_500(rock) - 1)
	settled = False
	while not settled and drop_point.imag < floor:
		if (drop_point + complex(0, 1)) not in rock:
			drop_point = drop_point + complex(0,1)
		elif (drop_point + complex(-1, 1)) not in rock:
			drop_point = drop_point + complex(-1, 1)
		elif (drop_point + complex(1, 1)) not in rock:
			drop_point = drop_point + complex(1, 1)
		else:
			rock.append(drop_point)
			sand.append(drop_point)
			settled = True
	if drop_point.imag >= floor:
		done = True
print(len(sand))
