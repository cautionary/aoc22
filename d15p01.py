import re

input = open('d15i01.txt', 'r')
lines = input.read()

TARGET = 2000000

target_row = set()
beacons_in_target = set()


for line in lines.strip().split("\n"):
    matches = re.match("Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(\d+)", line)
    sensor, beacon = complex(int(matches[1]), int(matches[2])), complex(int(matches[3]), int(matches[4]))

    if beacon.imag == TARGET:
        beacons_in_target.add(beacon)

    distance = sensor - beacon
    mdist = int(abs(distance.real) + abs(distance.imag))

    dist_to_target = int(abs(sensor.imag - TARGET))

    width_at_target = max(0, (mdist * 2 + 1) - (2 * dist_to_target))

    for i in range(int(sensor.real) - width_at_target // 2, 1 + int(sensor.real) + width_at_target // 2):
        target_row.add(i)


print(len(target_row) - len(beacons_in_target))
