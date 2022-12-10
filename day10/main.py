lines = open('main.in', 'r').read().splitlines()

X = 1
cycles = 0
last_cycles = 0
a = [20, 60, 100, 140, 180, 220]
N = 6
M = 40
grid = [['.' for i in range(M)] for j in range(N)]
print(grid)

def f(x):
    row, col = x // M, x % M
    ret = [(row, col)]
    if col - 1 >= 0 and col - 1 < M:
        ret.append((row,col-1))
    if col + 1 >= 0 and col + 1 < M:
        ret.append((row,col+1))
    return ret

def help(x):
    #print('x', x)
    return [x // M, x % M]

deargod = {}
ans = 0
for line in lines:
    if line == 'noop':
        cycles += 1
        if cycles in a:
            print(cycles, X)
            ans += cycles * X
        deargod[cycles] = X

    elif line.startswith('addx'):
        cycles += 2
        b = None
        r,c = help(cycles - 1)
        if cycles in a:
            b = cycles
        elif(cycles - 1) in a:
            b = cycles - 1
        if b:
            print(b, X, b*X)
            ans += b * X
        deargod[cycles - 1] = X
        X += int(line.split(' ')[1])
        deargod[cycles] = X

for i in range(cycles):
    r, c = help(i)
    if not i:
        grid[0][0] = '#'
        continue
    rr, cc = help(deargod[i])
    print(i, r, c, rr, cc, deargod[i])
    for row, col in f(rr*M + cc):
        if col == c:
            print(i)
            grid[r][c] = '#'

for i in grid:
    print(*i)
