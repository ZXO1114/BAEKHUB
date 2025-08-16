c = int(input())
k, b = map(int,input().split())

if k//2 + b <= c:
    print(k//2 + b)
else:
    print(c)