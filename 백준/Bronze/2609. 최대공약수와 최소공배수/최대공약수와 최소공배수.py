a,b = map(int,input().split())

if a > b:
    a, b = b, a

h = a
for i in range(a,0,-1):
    if a % i == 0 and b % i ==0:
        print(i)
        break

while True:
    if h % b == 0:
        print(h)
        break
    else:
        h += a