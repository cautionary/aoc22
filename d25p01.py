f = open("d25i01.txt")
lines = f.readlines()

sum = 0
for line in lines:
    dec = 0
    exp = 0
    line = line.strip()
    for i in range(len(line) - 1, -1, -1):
        dig = line[i]
        if dig == '-':
            dig = -1
        elif dig == '=':
            dig = -2
        else:
            dig = int(dig)
        dec += dig * 5 ** exp
        exp += 1

    sum += dec
        

exp = 0

exp_found = False
while not exp_found:
    total = 0
    for i in range(exp + 1):
        total += (5 ** i) * 2
    if sum <= total:
        exp_found = True
    else:
        exp += 1

digits = ""
worknum = sum
for i in range(exp, -1, -1):
    oexps = 0
    for n in range(i-1, -1, -1):
        oexps += 5 ** n * 2
        
    if worknum >= 5 ** i * 2 - oexps:
        digits += "2"
        worknum -= 5 ** i * 2
    elif worknum >= 5 ** i - oexps:
        digits += "1"
        worknum -= 5 ** i
    elif worknum >= -1 * oexps:
        digits += "0"
    elif worknum >= -1 * (5 ** i + oexps):
        digits += "-"
        worknum += 5 ** i
    elif worknum >= -1 * (5 ** i * 2 + oexps):
        digits += "="
        worknum += 5 ** i * 2

print(digits)

#    3125    625   125   25   5   1
# = -6250   -1250 -250  -50  -10 -2 
# - -3125    -625  -125  -25  -5 -1
# 0   0       0     0    0    0   0
# 1  3125     625  125   25   5   1
# 2  6250    1250  250   50   10  2
#
#    2=-1=0

