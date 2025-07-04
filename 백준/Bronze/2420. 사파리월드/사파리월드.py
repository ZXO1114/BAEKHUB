a,b = map(int,input().split())
a -= b
if a < 0:
    a *= -1
print(a)