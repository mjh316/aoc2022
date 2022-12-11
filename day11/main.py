lines = open('main.in', 'r').read().splitlines()
import sys
sys.set_int_max_str_digits(1000000)

monkeys = []

class Monkey:
    def __init__(self, items, op, test, t, f):
        self.items = items
        self.op = op
        self.test = test
        self.t = t
        self.f = f 
        self.inspects = 0

    def __repr__(self):
        return f'{self.items}'
    
    def bruh(self):
        global monkeys
        for item in self.items:
            old = item
            ret = eval(self.op.replace('new =', '').replace('old', str(item)).strip()) % BIGMOD
            if ret % self.test == 0:
                monkeys[self.t].items.append(ret)
            else:
                monkeys[self.f].items.append(ret)
            self.inspects += 1
        self.items = []

i = 0
rounds = 0 
#print(lines)
while i < len(lines):
    if len(lines[i]) == 0:
        i += 1
    #print(i)
    i += 1
    items = list(map(int, lines[i].split(': ')[1].split(', ')))
    i += 1
    op = lines[i].split(': ')[1]
    i += 1
    test = int(lines[i].split(' ')[-1])
    print('test', test)
    i += 1
    true = int(lines[i].split('monkey ')[1])
    i += 1
    false = int(lines[i].split('monkey ')[1])
    monkeys.append(Monkey(items, op, test, true, false))
    i += 1
BIGMOD = 1

for monkey in monkeys:
    BIGMOD *= monkey.test

print(BIGMOD)

ans = 1
helpb=[]
while rounds < 10000:
    for monkey in monkeys:
        monkey.bruh()
    #print(monkeys)
    rounds += 1

for monkey in monkeys:
    #print(monkey.inspects)
    helpb.append(monkey.inspects)
    #ans *= monkey.inspects
print(helpb)
helpb.sort()
print(helpb[-1]*helpb[-2])
