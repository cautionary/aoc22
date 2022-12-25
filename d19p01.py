import re
import random

f =  open('d19i01.txt','r')
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

best = [ 0 for _ in range(len(blueprints) + 1) ]
while True:
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

            move_taken = False
            while not move_taken:
                inp = random.randint(0,4)
                if inp == 0:
                    move_taken = True
                elif inp == 1 \
                        and inventory['ore'] >= bp['orebot']['ore']:
                    work_queue.append('orebot')
                    inventory['ore'] -= bp['orebot']['ore']
                    move_taken = True
                elif inp == 2 \
                        and inventory['ore'] >= bp['claybot']['ore']:
                    work_queue.append('claybot')
                    inventory['ore'] -= bp['claybot']['ore']
                    move_taken = True
                elif inp == 3 \
                        and inventory['ore'] >= bp['obsidianbot']['ore'] \
                        and inventory['clay'] >= bp['obsidianbot']['clay']:
                    work_queue.append('obsidianbot')
                    inventory['ore'] -= bp['obsidianbot']['ore']
                    inventory['clay'] -= bp['obsidianbot']['clay']
                    move_taken = True
                elif inp == 4 \
                        and inventory['ore'] >= bp['geodebot']['ore'] \
                        and inventory['obsidian'] >= bp['geodebot']['obsidian']:
                    work_queue.append('geodebot')
                    inventory['ore'] -= bp['geodebot']['ore']
                    inventory['obsidian'] -= bp['geodebot']['obsidian']
                    move_taken = True

            inventory['ore'] += inventory['orebot']
            inventory['clay'] += inventory['claybot']
            inventory['obsidian'] += inventory['obsidianbot']
            inventory['geode'] += inventory['geodebot']

            if len(work_queue) > 0:
                inventory[work_queue.pop(0)] += 1

        best[bp['id']] = max(best[bp['id']], inventory['geode'] * bp['id'])
    print(best, sum(best))
        
#1461 too low
