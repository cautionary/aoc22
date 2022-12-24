import re
import functools

f =  open('d16s01.txt','r')
lines = f.readlines()

def get_states(valves, states):
    new_states = []
    for state in states:
        cur = state['cur']
        neighbors = valves[cur]['neighbors']
        if valves[cur]['flow'] > 0 and cur not in state['opens']:
            new_states.append({'cur': cur, 
                               'flow': state['flow'] + valves[cur]['flow'],
                               'opens': state['opens'] + [cur],
                               'rem_min': state['rem_min'] - 1,
                               'released': state['released'] + state['flow']})
        for neighbor in neighbors:
            new_states.append({'cur': neighbor,
                               'flow': state['flow'],
                               'opens': state['opens'],
                               'rem_min': state['rem_min'] - 1,
                               'released': state['released'] + state['flow']})
    return new_states

#def paths_to_valves(valves, cur, rem_min):
#    valves = dict(sorted(valves.items(), key=lambda item: item[1]["flow"], reverse=True))
#    possible_targets = []
#    for valve in valves:
#        if valves[valve]["flow"] > 0 and valves[valve]["state"] == 0:
#            possible_targets.append((valve, valves[valve]["flow"]))
#
#    possible_targets = sorted(possible_targets, key = lambda x: x[1], reverse=True)
#    return (cur, 0, [cur])

@functools.lru_cache()
def shortest_path(valves, start, target):
    unvisited = []
    visited = []
    distances = {}
    for valve in valves:
        distances[valve] = 1000
        unvisited.append(valve)
    distances[start] = 0
    cur = start
    paths = {}
    route = []
    while len(unvisited) > 0:
        unvisited.remove(cur)
        visited.append(cur)
        
        for neighbor in valves[cur]["neighbors"]:
            if distances[cur] + 1 < distances[neighbor]:
                distances[neighbor] = distances[cur] + 1
                paths[neighbor] = cur
        
        cur = None
        for valve in unvisited:
            if cur is None:
                cur = valve
            elif distances[valve] < distances[cur]:
                cur = valve 

    node = target
    while node != start:
        try:
            route.insert(0, node)
            node = paths[node]
        except Exception:
            break
    return(route)

valves = {}

for line in lines:
    matches = re.match("Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", line)
    valve = matches[1]
    flow = int(matches[2])
    neighbors = matches[3].split(", ")
    
    valves[valve] = {"flow": flow, "neighbors": neighbors, "state": 0}

current_valve = "AA"

flows = []
pressure = 0

states = [{'cur': 'AA', 'flow': 0, 'opens': [], 'rem_min': 30, 'released': 0}]
for minute in range(30):
    print(minute)
    states = get_states(valves, states)

for state in states:
    print(state['released'])
