import re
from functools import lru_cache

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
#inventory = (ore, clay, obs, geode, orbot, cbot, obbot, gbot)
invmap = ['ore', 'clay', 'obsidian', 'geode', 'orebot', 'claybot', 'obsidianbot', 'geodebot']

@lru_cache(maxsize=None)
def get_results(minutes, bpid, inventory):
    global blueprints
    bp = blueprints[bpid]

    if minutes <= 0:
        return 0

    result = 0

    inventory = list(inventory)

    possible_buys = []

    waiting = False
    if inventory[0] >= bp['orebot']['ore']:
        if inventory[4] < max(bp['claybot']['ore'], bp['obsidianbot']['ore'], bp['geodebot']['ore']):
            possible_buys.append('orebot')
    else:
        waiting = True
    if inventory[0] >= bp['claybot']['ore']:
        if inventory[5] < bp['obsidianbot']['clay']:
            possible_buys.append('claybot')
    else:
        waiting = True
    if inventory[0] >= bp['obsidianbot']['ore'] \
      and inventory[1] >= bp['obsidianbot']['clay']:
        if inventory[6] < bp['geodebot']['obsidian']:
            possible_buys.append('obsidianbot')
    else:
        waiting = True
    if inventory[0] >= bp['geodebot']['ore'] \
      and inventory[2] >= bp['geodebot']['obsidian']:
        possible_buys.append('geodebot')
    else:
        waiting = True

    if waiting:
        possible_buys.append(-1)

    for i in range(4, 8):
        inventory[i-4] += inventory[i]

    if inventory[0] > 25:
        inventory[0] = 25
    if inventory[1] > 35:
        inventory[1] = 35
    
    newgbot = 0
    for pbuy in possible_buys:
        tinv = inventory.copy()
        if pbuy == -1:
            result = max(result, get_results(minutes - 1, bpid, tuple(inventory)))
        else:
            for cost in bp[pbuy]:
                tinv[invmap.index(cost)] -= bp[pbuy][cost]
            tinv[invmap.index(pbuy)] += 1
            if pbuy == "geodebot":
                newgbot = 1
            for i in range(4):
                if inventory[i] < 0:
                    print(bpid, minutes, pbuy, inventory)
            result = max(result, get_results(minutes - 1, bpid, tuple(tinv)) + (newgbot * (minutes - 1)))

    return result

prod = 1

for i in range(3):
    res = get_results(32, i, (0,0,0,0,1,0,0,0))
    prod = prod * res

print(prod)
