import re

input = open('d15s01.txt', 'r')
lines = input.read()

MIN = 0
MAX = 20 #4000000

coverage = set()

c = 0
for line in lines.strip().split("\n"):
    print(c)
    c += 1
    matches = re.match("Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(\d+)", line)
    sensor, beacon = complex(int(matches[1]), int(matches[2])), complex(int(matches[3]), int(matches[4]))
    coverage.add(sensor)
    coverage.add(beacon)

    distance = sensor - beacon
    mdist = int(abs(distance.real) + abs(distance.imag))

    for i in range(mdist + 1):
        q1 = sensor + complex(i, mdist - i)
        q2 = sensor + complex(i, -(mdist - i))
        q3 = sensor + complex(-i, mdist - i)
        q4 = sensor + complex(-i, -(mdist - i))

        #print((sensor, mdist, i, k, q1, q2, q3, q4))

        if q1.real >= MIN and q1.real <= MAX and q1.imag >= MIN and q1.imag <+ MAX:
            coverage.add(q1)
        if q2.real >= MIN and q2.real <= MAX and q2.imag >= MIN and q2.imag <+ MAX:
            coverage.add(q2)
        if q3.real >= MIN and q3.real <= MAX and q3.imag >= MIN and q3.imag <+ MAX:
            coverage.add(q3)
        if q4.real >= MIN and q4.real <= MAX and q4.imag >= MIN and q4.imag <+ MAX:
            coverage.add(q4)


for i in range(MAX):
    for j in range(MAX):
        if complex(i,j) not in coverage:
            print((i,j))
