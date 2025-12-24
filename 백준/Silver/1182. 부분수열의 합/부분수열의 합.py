import sys
input = sys.stdin.readline

# def crazy():

n, s = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
h = 1
c = 0

while h < 2**n:
    o = [b for b in bin(h)[2:].zfill(n)]
    h += 1
    if sum([l[num] for num in range(n) if o[num] == '1']) == s:
        c += 1
print(c)



