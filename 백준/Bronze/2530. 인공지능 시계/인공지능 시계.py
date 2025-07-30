h, m, s = map(int,input().split())
s += int(input())

while s >= 60:
    s -= 60
    m += 1
    if m == 60:
        m -= 60
        h += 1
        if h == 24:
            h = 0
print(h, m, s)