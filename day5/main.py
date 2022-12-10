lines = open('main.in', 'r').read().splitlines()

a=[
    'W D G B H R V'.split(' '),
    'J N G C R F'.split(' '),
    'L S F H D N J'.split(' '),
    'J D S V'.split(' '),
    'S H D R Q W N V'.split(' '),
    'P G H C M'.split(' '),
    'F J B G L Z H C'.split(' '),
    'S J R'.split(' '),
    'L G S R B N V M'.split(' ')
]

for line in lines:
    b = input().split(' ')
    i1,i2,i3 = int(b[1]), int(b[3]), int(b[5])
    tmp = []
    for i in range(i1):
        tmp.append(a[i2-1][-1])
        a[i2-1].pop()
    a[i3-1].extend(list(reversed(tmp)))

for i in a:
    print(i[-1])
