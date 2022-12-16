input = open('d08i01.txt', 'r')
lines = input.readlines()

#lines = ["30373", "25512", "65332", "33549", "35390"]

for i in range(len(lines)):
    lines[i] = lines[i].strip()

max_scenic = 0

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        this_height = int(lines[i][j])
        
        scenic_up = 1
        k = i - 1
        while k > 0 and int(lines[k][j]) < this_height:
            scenic_up += 1
            k -= 1

        scenic_down = 1
        k = i + 1
        while k < len(lines)-1 and int(lines[k][j]) < this_height:
            scenic_down += 1
            k += 1

        scenic_left = 1
        k = j - 1
        while k > 0 and int(lines[i][k]) < this_height:
            scenic_left += 1
            k -= 1

        scenic_right = 1
        k = j + 1
        while k < len(lines[0])-1 and int(lines[i][k]) < this_height:
            scenic_right += 1
            k += 1

        max_scenic = max(max_scenic, scenic_up * scenic_down * scenic_left * scenic_right)

        print((scenic_up, scenic_down, scenic_left, scenic_right))
print(max_scenic)

#361920 too low
