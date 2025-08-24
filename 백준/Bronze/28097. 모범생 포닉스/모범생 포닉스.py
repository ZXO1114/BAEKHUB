l = int(input())
l = list(map(int,input().split()))
l = (sum(l)+((len(l)-1)*8))
h = 0
while l >= 24:
    h += 1
    l -= 24
print(h,l)