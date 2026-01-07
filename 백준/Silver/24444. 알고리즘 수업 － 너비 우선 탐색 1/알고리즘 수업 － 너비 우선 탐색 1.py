import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    queue = deque([r])
    visited = [-1] + [0] * n
    c = 0
    while queue:
        tmp = queue.popleft()
        if visited[tmp] == 0:
            c += 1
            visited[tmp] = 1
            order[tmp] = c
            queue.extend(graph[tmp])

n,m,r = map(int,input().strip().split())
graph = [-1]+[[] for i in range(n)]

for _ in range(m):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1): graph[i].sort()
order = [-1] + [0] * n
dfs()
print('\n'.join(map(str,order[1:])))