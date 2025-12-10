import sys
input = sys.stdin.readline
# min max 활용
n = int(input())
l = [0,0]
for num in range(2,n+1):
    # print(num)
    if num % 6 == 0:
        h = min(l[num//2],l[num//3],l[num-1]) + 1
    elif num % 2 == 0:
        h = min(l[num // 2], l[num - 1]) + 1
    elif num % 3 == 0:
        h = min(l[num // 3], l[num - 1]) + 1
    else:
        h = l[num - 1] + 1
    l.append(h)
print(l[n])