import re
from functools import lru_cache

f =  open('d16i01.txt','r')

lines = f.readlines()

valves = {}

for line in lines:
    matches = re.match("Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", line)
    valve = matches[1]
    flow = int(matches[2])
    neighbors = matches[3].split(", ")
    
    valves[valve] = {"flow": flow, "neighbors": neighbors}

@lru_cache(maxsize=None)
def get_result(minutes, pos, epos, opens):
    if minutes <= 1:
        return 0
    result = 0

    if pos not in opens and valves[pos]['flow'] > 0 \
      and epos not in opens and valves[epos]['flow'] > 0 \
      and pos != epos:
        opens = tuple(sorted([*opens, pos, epos]))
        result = max(result, get_result(minutes - 1, pos, epos, opens) + (valves[pos]['flow'] + valves[epos]['flow']) * (minutes - 1))
        
    elif pos not in opens and valves[pos]['flow'] > 0:
        opens = tuple(sorted([*opens, pos]))
        for neighbor in valves[epos]['neighbors']:
            result = max(result, get_result(minutes - 1, pos, neighbor, opens) + valves[pos]['flow'] * (minutes - 1))

    elif epos not in opens and valves[epos]['flow'] > 0:
        opens = tuple(sorted([*opens, epos]))
        for neighbor in valves[pos]['neighbors']:
            result = max(result, get_result(minutes - 1, neighbor, epos, opens) + valves[epos]['flow'] * (minutes - 1))

    else:
        for neighbor in valves[pos]['neighbors']:
            for eneighbor in valves[epos]['neighbors']:
                result = max(result, get_result(minutes - 1, neighbor, eneighbor, opens))
    
    return result

print(get_result(26, 'AA', 'AA', ()))


