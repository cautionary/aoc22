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
def get_result(minutes, pos, opens):
    if minutes <= 1:
        return 0
    result = 0
    for neighbor in valves[pos]['neighbors']:
        result = max(result, get_result(minutes - 1, neighbor, opens))
    if pos not in opens and valves[pos]['flow'] > 0:
        opens = tuple(sorted([*opens, pos]))
        result = max(result, get_result(minutes - 1, pos, opens) + valves[pos]['flow'] * (minutes - 1))
    return result

print(get_result(30, 'AA', ()))


#def shortest_path(start, target):
#    global valves
#    unvisited = []
#    visited = []
#    distances = {}
#    for valve in valves:
#        distances[valve] = 1000
#        unvisited.append(valve)
#    distances[start] = 0
#    cur = start
#    paths = {}
#    route = []
#    while len(unvisited) > 0:
#        unvisited.remove(cur)
#        visited.append(cur)
#        
#        for neighbor in valves[cur]["neighbors"]:
#            if distances[cur] + 1 < distances[neighbor]:
#                distances[neighbor] = distances[cur] + 1
#                paths[neighbor] = cur
#        
#        cur = None
#        for valve in unvisited:
#            if cur is None:
#                cur = valve
#            elif distances[valve] < distances[cur]:
#                cur = valve 
#
#    node = target
#    while node != start:
#        try:
#            route.insert(0, node)
#            node = paths[node]
#        except Exception:
#            break
#    return(route)
#
