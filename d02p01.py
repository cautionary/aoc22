infile = open('d02i01.txt', 'r')

lines = infile.readlines()

score = 0

#A,X = 1 = Rock
#B,Y = 2 = Paper
#C,Z = 3 = Scissors

for line in lines:
    line = line.strip()
    plays = line.split()
    them = plays[0]
    me = plays[1]

    if me == 'X':
        score += 1
        if them == 'A':
            score += 3
        elif them == 'C':
            score += 6
    elif me == 'Y':
        score += 2
        if them == 'B':
            score += 3
        elif them == 'A':
            score += 6
    elif me == 'Z':
        score += 3
        if them == 'C':
            score += 3
        elif them == 'B':
            score += 6
            
print(score)
