f = list(map(int,input().split()))
m = f[0]/f[1]
for i in range(int(input())):
    a,b = map(int,input().split())
    if a/b < m:
        m = a/b
print(f"{m*1000:.2f}")