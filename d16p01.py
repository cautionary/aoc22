import re
from itertools import permutations

f =  open('d16i01.txt','r')
lines = f.readlines()

def paths_to_valves(valves, cur, rem_min):
    valves = dict(sorted(valves.items(), key=lambda item: item[1]["flow"], reverse=True))
    possible_targets = []
    for valve in valves:
        if valves[valve]["flow"] > 0 and valves[valve]["state"] == 0:
            possible_targets.append((valve, valves[valve]["flow"]))

    possible_targets = sorted(possible_targets, key = lambda x: x[1], reverse=True)

    if len(possible_targets) > 0:
        highest_value = 0
        winning_opt = None
        opts = list(permutations(range(min(4, len(possible_targets)))))
        for o in opts:
            pts = []
            for p in range(len(o)):
                pts.append(possible_targets[o[p]][0])
            paths = [shortest_path(valves, cur, pts[0])]
            for p in range(len(o)-1):
                paths.append(shortest_path(valves, pts[p], pts[p+1]))
            values = []
            for p in range(len(o)):
                rm = rem_min
                for v in range(p+1):
                    rm = rm - len(paths[v])
                values.append(max(0, rm * possible_targets[o[p]][1]))
            value = sum(values)

            if value > highest_value:
                    highest_value = value
                    winning_opt = o
        #print((winning_opt, possible_targets))

        return (possible_targets[winning_opt[0]][0], possible_targets[winning_opt[0]][1], shortest_path(valves, cur, possible_targets[winning_opt[0]][0]))
    else:
        return (cur, 0, [cur])

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

for minute in range(30):
    print((minute, current_valve, flows))

    for flow in flows:
        pressure = pressure + flow

    next_valve = paths_to_valves(valves, current_valve, 30 - minute)
    #print(next_valve)
    if next_valve and next_valve[0] != current_valve:
        current_valve = next_valve[2][0]
    elif valves[current_valve]["state"] == 0:
        valves[current_valve]["state"] = 1
        flows.append(valves[current_valve]["flow"])

    print(pressure)
