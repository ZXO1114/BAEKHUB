n = int(input())
for i in range(n):
    A, B, X = map(int,input().split())
    print((A*(X-1))+B)