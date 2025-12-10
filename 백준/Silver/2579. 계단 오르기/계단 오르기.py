import sys
input = sys.stdin.readline

n = int(input())
l = [0]

for _ in range(n): l.append(int(input()))
if n == 1:
    print(l[-1])
else:
    stair = [0,l[1],l[1]+l[2]]
    for i in range(3,n+1):
        stair.append(max(l[i]+l[i-1] + stair[i-3], l[i] + stair[i-2]))
    print(stair[-1])

