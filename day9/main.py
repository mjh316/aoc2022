st = set()
headst = set()

lines = open('main.in', 'r').read().splitlines()

bruh = [[1000,1000]]
for i in range(1, 10):
    bruh.append([bruh[0][0], bruh[0][1]])
st.add(f'{bruh[-1][0]} {bruh[-1][1]}')

def get_dir(i):
    row, col = bruh[i-1]
    tr, tc = bruh[i]
    if col == tc and row < tr:
        return 'N'
    if col > tc and row < tr:
        return 'NE'
    if row == tr and col > tc:
        return 'E'
    if row > tr and col > tc:
        return 'SE'
    if row > tr and col == tc:
        return 'S'
    if row > tr and col < tc:
        return 'SW'
    if row == tr and col < tc:
        return 'W'
    if row < tr and col < tc:
        return 'NW'

def touching(i):
    mp = {
        'N': (-1, 0),
        'NE': (-1, 1),
        'E': (0, 1),
        'SE': (1, 1),
        'S': (1, 0),
        'SW': (1, -1),
        'W': (0, -1),
        'NW': (-1, -1)
    }
    for key in mp:
        rr, cc = bruh[i-1][0] + mp[key][0], bruh[i-1][1] + mp[key][1]
        if rr == bruh[i][0] and cc == bruh[i][1]:
            return True
    if bruh[i-1][0] == bruh[i][0] and bruh[i-1][1] == bruh[i][1]:
        return True
    return False

def catch_up(d, i):
    mp = {
        'N': (-1, 0),
        'NE': (-1, 1),
        'E': (0, 1),
        'SE': (1, 1),
        'S': (1, 0),
        'SW': (1, -1),
        'W': (0, -1),
        'NW': (-1, -1)
    }
    #print(i)
    #print(bruh[i][0])
    bruh[i][0] += mp[d][0]
    bruh[i][1] += mp[d][1]

def move(direction, dist):
    global st
    while dist > 0:
        match direction:
            case 'U':
                bruh[0][0] -= 1
            case 'D':
                bruh[0][0] += 1
            case 'L':
                bruh[0][1] -= 1
            case 'R':
                bruh[0][1] += 1
        headst.add(f'{bruh[0][0]} {bruh[0][1]}')
        for i in range(1, 10):
            if touching(i):
                continue
            catch_up(get_dir(i), i)
        st.add(f'{bruh[-1][0]} {bruh[-1][1]}')
        dist -= 1

for line in lines:
    d, dist = line.split(' ')
    #st.add((tr, tc))
    move(d, int(dist))
    #print(bruh)

for i in range(900, 1400):
    for j in range(900, 1400):
        print('#' if f'{i} {j}' in st else '.', end='')
    print()

print(len(st))

