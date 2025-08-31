n, x = map(int,input().split())
l = list(map(int,input().split()))
n_min = 0
for i in range(n-1):
    if l[i]+l[i+1] < n_min : n_min = l[i]+l[i+1]
    elif n_min == 0: n_min = l[i]+l[i+1]
print(n_min*x)
