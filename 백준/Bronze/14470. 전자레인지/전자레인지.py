a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = 0
while a < b:
    if a < 0:
        a += 1
        t += c
    else:
        if a == 0:
            t += d
        a += 1
        t += e
print(t)