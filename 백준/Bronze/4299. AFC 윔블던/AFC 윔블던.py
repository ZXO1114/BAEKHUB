a,b = map(int,input().split())
x = (a+b)/2
y = (a-b)/2

if (x >=0 and y >=0) and x == int(x):
    if x >= y:
        print(int(x),int(y))
    else:
        print(int(y),int(x))
else:
    print(-1)

