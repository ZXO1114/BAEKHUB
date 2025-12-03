import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    h = tuple(map(int,input().strip().split()))
    l.append(h)

l.sort(key=lambda x:(x[1],x[0]))
end = l[0][1]
c = 1

for cf in l[1:]:
    if cf[0] >= end:
        end = cf[1]
        c += 1
print(c)