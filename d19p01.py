import re

f =  open('d19s01.txt','r')
lines = f.readlines()

blueprints = []
for line in lines:
    matches = re.match("Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", line)
    bp = {'id': int(matches[1]), 
          'orebot': {'ore': int(matches[2])}, 
          'claybot': {'ore': int(matches[3])}, 
          'obsidianbot': {'ore': int(matches[4]), 'clay': int(matches[5])},
          'geodebot': {'ore': int(matches[6]), 'obsidian': int(matches[7])}}
    blueprints.append(bp)

results = {}
for bp in blueprints:
    inventory = {'orebot': 1,
                 'claybot': 0,
                 'obsidianbot': 0,
                 'geodebot': 0,
                 'ore': 0,
                 'clay': 0,
                 'obsidian': 0,
                 'geode': 0}
    work_queue = []
    for min in range(24):
        print(min, inventory)

        if inventory['obsidian'] >= bp['geodebot']['obsidian'] \
          and inventory['ore'] >= bp['geodebot']['ore']:
            work_queue.append('geodebot')
            inventory['ore'] -= bp['geodebot']['ore']
            inventory['obsidian'] -= bp['geodebot']['obsidian']
        elif inventory['obsidianbot'] < 2 \
          and inventory['ore'] >= bp['obsidianbot']['ore'] \
          and inventory['clay'] >= bp['obsidianbot']['clay']:
            work_queue.append('obsidianbot')
            inventory['ore'] -= bp['obsidianbot']['ore']
            inventory['clay'] -= bp['obsidianbot']['clay']
        elif inventory['claybot'] < 4 \
          and inventory['ore'] >= bp['claybot']['ore']:
            work_queue.append('claybot')
            inventory['ore'] -= bp['claybot']['ore']
        elif inventory['orebot'] < 1 \
          and inventory['ore'] >= bp['orebot']['ore']:
            work_queue.append('orebot')
            inventory['ore'] -= bp['orebot']['ore']

        inventory['ore'] += inventory['orebot']
        inventory['clay'] += inventory['claybot']
        inventory['obsidian'] += inventory['obsidianbot']
        inventory['geode'] += inventory['geodebot']

        if len(work_queue) > 0:
            inventory[work_queue.pop(0)] += 1
        
    print(inventory)
