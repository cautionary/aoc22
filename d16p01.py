import re

f =  open('d16s01.txt','r')
lines = f.readlines()

def paths_to_valves(valves, cur, rem_min):
	valves = dict(sorted(valves.items(), key=lambda item: item[1]["flow"], reverse=True))
	possible_targets = []
	for valve in valves:
		if valves[valve]["flow"] > 0 and valves[valve]["state"] == 0:
			path_to_target = shortest_path(valves, cur, valve)
			value = valves[valve]["flow"] * (rem_min - len(path_to_target))
			print((valve, valves[valve]["flow"], rem_min, len(path_to_target), value))
			possible_targets.append((valve, value, path_to_target))
	target = None
	print(possible_targets)
	for t in possible_targets:
		if target is None:
			target = t
		elif t[1] >= target[1] and len(t[2]) < len(target[2]):
			target = t
	return target



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

for minute in range(1, 30):
	print((minute, current_valve, flows))

	for flow in flows:
		pressure = pressure + flow

	next_valve = paths_to_valves(valves, current_valve, 30 - minute)
	print(next_valve)
	if next_valve and next_valve[0] != current_valve:
		current_valve = next_valve[2][0]
	else:
		valves[current_valve]["state"] = 1
		flows.append(valves[current_valve]["flow"])

print(pressure)
