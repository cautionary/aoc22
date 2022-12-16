import re

input = open('d15i01.txt', 'r')
lines = input.read()

MAX = 4000000
coverage = []

for r in range(MAX):
    if r % 10000 == 0:
        print(r)
    coverage.append([])
    for line in lines.strip().split("\n"):
        matches = re.match("Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(\d+)", line)
        sensor, beacon = complex(int(matches[1]), int(matches[2])), complex(int(matches[3]), int(matches[4]))
    
        distance = sensor - beacon
        mdist = int(abs(distance.real) + abs(distance.imag))
    
        dist_to_target = int(abs(sensor.imag - r))

        width_at_target = max(0, (mdist * 2 + 1) - (2 * dist_to_target))

        if width_at_target > 0:
            target_range = (max(0, int(sensor.real) - width_at_target // 2), min(MAX, int(sensor.real) + width_at_target // 2))

            coverage[r].append(target_range)

    combined_ranges = coverage[r]
    old_cr = []
    while old_cr != combined_ranges:
        old_cr = combined_ranges.copy()
        pair = combined_ranges[0]
        found_pair = False
        if len(combined_ranges) > 1:
            while not found_pair:
                 for other_pair in combined_ranges[1:]:
                     if not found_pair:
                         if (pair[0] <= other_pair[1] and pair[1] >= other_pair[0]) \
                           or (pair[1] >= other_pair[0] and pair[0] <= other_pair[1]):
  
                             new_pair = (min(pair[0], other_pair[0]), max(pair[1], other_pair[1]))
                             combined_ranges.remove(pair)
                             combined_ranges.remove(other_pair)
                             combined_ranges.append(new_pair)
                             found_pair = True
                 if not found_pair:
                     print((r, combined_ranges))
                     for cr in combined_ranges:
                         if cr[0] == 0:
                             y = r
                             x = cr[1] + 1
                             print(x * 4000000 + y)
                     exit() 

for r in range(MAX):
    if r % 10000 == 0:
        print(r)
    combined_ranges = coverage[r]
    old_cr = []
    while old_cr != combined_ranges:
        old_cr = combined_ranges.copy()
        pair = combined_ranges[0]
        found_pair = False
        if len(combined_ranges) > 1:
            while not found_pair:
                 for other_pair in combined_ranges[1:]:
                     if not found_pair:
                         if (pair[0] <= other_pair[1] and pair[1] >= other_pair[0]) \
                           or (pair[1] >= other_pair[0] and pair[0] <= other_pair[1]):
  
                             new_pair = (min(pair[0], other_pair[0]), max(pair[1], other_pair[1]))
                             combined_ranges.remove(pair)
                             combined_ranges.remove(other_pair)
                             combined_ranges.append(new_pair)
                             found_pair = True
                 if not found_pair:
                     print((r, combined_ranges))
                     for cr in combined_ranges:
                         if cr[0] == 0:
                             y = r
                             x = cr[1] + 1
                             print(x * 4000000 + y)
                     exit() 


