lines = open('main.in', 'r').read().splitlines()
i=0

for line in lines:
    a, b = line.split(',')
    a = list(map(int, a.split('-')))
    b = list(map(int, b.split('-')))
    #print(a,b, b[0] <= a[0], b[0] >= a[1], a[0] <= b[0], a[1] >= b[1])
    if a[0] > b[0]:
        tmp = a
        a = b
        b = tmp
    if b[0] <= a[1]:
        i += 1
print(i)
