n = int(input())
h = 1
t = 0
while n != 0:
    if n >= h:
        n -= h
        h += 1
        t += 1
    else:
        h = 1
print(t)