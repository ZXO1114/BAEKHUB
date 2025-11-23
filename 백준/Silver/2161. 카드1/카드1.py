import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque(range(1,n+1))

while True:
    print(d.popleft(),end = ' ')
    if len(d) == 0:
        break
    d.append(d.popleft())