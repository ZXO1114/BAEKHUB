n = int(input())
h = 1001
for i in range(n):
    a,b = map(int,input().split())
    if h > b >= a:
        h = b
if h == 1001:
    print(-1)
else:
    print(h)