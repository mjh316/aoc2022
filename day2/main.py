lines = open('main.in', 'r').readlines()
s=0
def be(x):
    match x:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3

for line in lines:
    # rock = a, paper = b, sicssors = c
    # x             y       z
    print(line.strip())
    op, me = line.strip().split(' ')
    # x is lose, y is draw, z is win
    if me == 'X': 
        if op == 'A':
            me = 'Z'
        elif op == 'B':
            me = 'X'
        elif op == 'C':
            me = 'Y'
    elif me == 'Y':
        if op == 'A':
            me = 'X'
        elif op == 'B':
            me = 'Y'
        elif op == 'C':
            me = 'Z'
    elif me == 'Z':
        if op == 'A':
            me = 'Y'
        elif op == 'B':
            me = 'Z'
        elif op == 'C':
            me = 'X'

    if me =='X': s += 0
    elif me == 'Y': s += 3
    elif me == 'Z': s += 6
    print(me)
    score = be(me)
    s += score
print(s)
