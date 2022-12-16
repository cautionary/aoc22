f =  open('d09i01.txt','r')

lines = f.readlines()

knots = []
for i in range(10):
	knots.append(0 + 0j)


t9_history = [knots[9]]

print(knots)

for line in lines:
	dir = line.strip().split()[0]
	num = int(line.strip().split()[1])

	for i in range(num):
		if dir == 'R':
			knots[0] = knots[0] + 1
		elif dir == 'L':
			knots[0] = knots[0] - 1
		elif dir == 'U':
			knots[0] = knots[0] + 1j
		elif dir == 'D':
			knots[0] = knots[0] - 1j

		for i in range(9):
			
			if knots[i].real == knots[i+1].real:
				if abs(knots[i].imag - knots[i+1].imag) > 1:
					if knots[i].imag > knots[i+1].imag:
						knots[i+1] = knots[i+1] + 1j
					else:
						knots[i+1] = knots[i+1] - 1j
			elif knots[i].imag == knots[i+1].imag:
				if abs(knots[i].real - knots[i+1].real) > 1:
					if knots[i].real > knots[i+1].real:
						knots[i+1] = knots[i+1] + 1
					else:
						knots[i+1] = knots[i+1] - 1
			elif abs(knots[i]-knots[i+1]) > abs(1 + 1j):
				if knots[i].imag > knots[i+1].imag:
					knots[i+1] = knots[i+1] + 1j
				else:
					knots[i+1] = knots[i+1] - 1j
	
				if knots[i].real > knots[i+1].real:
					knots[i+1] = knots[i+1] + 1
				else:
					knots[i+1] = knots[i+1] - 1
	
		if knots[9] not in t9_history:
			t9_history.append(knots[9])

print(len(t9_history))
