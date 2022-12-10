s=input()

def is_start(s, i):
    print(set(s[i:i+14]))
    return len(set(s[i:i+14])) == 14

i = 0
while i < len(s):
    if is_start(s, i):
        print(i+14)
        break
    i += 1
