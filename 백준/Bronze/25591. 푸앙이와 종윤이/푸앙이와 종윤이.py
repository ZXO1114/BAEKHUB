A,B = map(int,input().split())
a,b = 100-A,100-B
c,d = 100-(a+b),a*b
q,r = d//100, d%100
print(a,b,c,d,q,r)
if d<100:
    print(c,d)
else:
    print(c+q,r)
