n_max = 0
for i in range(int(input())):
    a,d,g = map(int,input().split())
    h = a*(d+g)
    if a == (d+g):h*=2
    if h > n_max: n_max = h
print(n_max)
