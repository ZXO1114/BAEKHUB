n = int(input())
l = list(map(int,input().split()))

l.sort()

if n % 2 == 0:
    print(l[0]*l[-1])
else:
    print(l[n//2]**2)