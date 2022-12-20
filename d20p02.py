f = open("d20i01.txt")
lines = f.readlines()

crypto_key = 811589153

original = []
num_count = {}
for line in lines:
    num = int(line.strip()) * crypto_key
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 0
    original.append((num, num_count[num]))

working = original.copy()

size = len(original)

for _ in range(10):
    for num in original:
        idx = working.index(num)
        working.pop(idx)
        new_pos = (idx + num[0]) % (size - 1)
        working.insert(new_pos, num)

start = working.index((0, 0))
answer = working[(start + 1000) % size][0] + working[(start + 2000) % size][0] + working[(start + 3000) % size][0]

print(answer)
