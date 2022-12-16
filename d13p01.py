import json

input = open('d13i01.txt', 'r')
lines = input.read()

pairs = lines.split("\n\n")

i = 0

total = 0

def isint(item):
    if isinstance(item, int):
        return True
    else:
        return False

def islist(item):
    if isinstance(item, list):
        return True
    else:
        return False

def compare_packets(p1, p2):
    for j in range(min(len(p1), len(p2))):
        if islist(p1[j]) or islist(p2[j]):
            if isint(p1[j]):
                temp_p1 = [p1[j]]
            else:
                temp_p1 = p1[j]
            if isint(p2[j]):
                temp_p2 = [p2[j]]
            else:
                temp_p2 = p2[j]
            if temp_p1 != temp_p2:
                return compare_packets(temp_p1, temp_p2)
        else:
            if p1[j] < p2[j]:
                return True
            elif p1[j] > p2[j]:
                return False
            
    if len(p1) < len(p2):
        return True
    elif len(p1) > len(p2):
        return False

for pair in pairs:
    i += 1
    packets = pair.split()

    packet1 = json.loads(packets[0])
    packet2 = json.loads(packets[1])

    if compare_packets(packet1, packet2):
        total += i

print(total)

