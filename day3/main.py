def f(x):
    if x == x.lower():
        return ord(x) - ord('a') + 1
    return ord(x) - ord('A') + 27
s=0
for i in range(100):
    a, b, c = input(), input(), input()
    x, y, z = set(a), set(b), set(c)
    d = x & y & z
    s += (f(list(d)[0]))
print(s)
