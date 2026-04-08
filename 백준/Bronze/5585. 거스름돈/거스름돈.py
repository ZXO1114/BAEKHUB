import sys
input = sys.stdin.readline

a = [500, 100, 50, 10, 5]
n = 1000 - int(input())
c = 0

for i in a:
    c += n // i
    n %= i

c += n

print(c)  