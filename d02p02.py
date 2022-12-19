infile = open('d02i01.txt', 'r')

lines = infile.readlines()

score = 0

#A = 1 = Rock
#B = 2 = Paper
#C = 3 = Scissors

#X = lose
#Y = draw
#Z = win

for line in lines:
    line = line.strip()
    plays = line.split()
    them = plays[0]
    me = plays[1]

    if them == 'A':
        if me == 'X':
            score += 3
        elif me == 'Y':
            score += 4
        elif me == 'Z':
            score += 8
    elif them == 'B':
        if me == 'X':
            score += 1
        elif me == 'Y':
            score += 5
        elif me == 'Z':
            score += 9
    elif them == 'C':
        if me == 'X':
            score += 2
        elif me == 'Y':
            score += 6
        elif me == 'Z':
            score += 7

print(score)
