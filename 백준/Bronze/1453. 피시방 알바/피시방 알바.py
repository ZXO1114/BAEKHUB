s = [None]+[0]*100
p = 0
n = int(input())
h = list(map(int,input().split()))
for i in h:
    if s[i] == 0:
        s[i] += 1
    else:
        p += 1
print(p)