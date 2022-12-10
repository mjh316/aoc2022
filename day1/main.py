a = open('main.in', 'r').readlines()
v=0
cur = 0
b=[]
for i in a:
    if i == '\n':
        b.append(cur)
        cur = 0
    else:
        cur += int(i.strip())
        v=max(v,cur)
b.sort(key=lambda x: -x)
print(b[0]+b[1]+b[2])
