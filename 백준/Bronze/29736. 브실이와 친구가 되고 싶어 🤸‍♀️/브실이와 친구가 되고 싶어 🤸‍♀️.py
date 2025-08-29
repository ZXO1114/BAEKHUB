n,m = map(int,input().split())
k,x = map(int,input().split())
h=0
if k-x > n:
    n = k-x
elif k+x < n:
    h = 1
if k+x < m:
    m = k+x
elif k-x > m:
    h = 1
if h ==0:
    print(m-n+1)
else:
    print('IMPOSSIBLE')