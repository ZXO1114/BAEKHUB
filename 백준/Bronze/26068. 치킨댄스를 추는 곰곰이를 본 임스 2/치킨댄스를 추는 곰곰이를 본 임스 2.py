r = 0
for i in range(int(input())):
    h = list(map(str,input().split('-')))
    if int(h[1]) <= 90: r += 1
print(r)