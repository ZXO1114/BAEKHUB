import sys
input = sys.stdin.readline

# def backtracking():
#     if len(array) == m:
#         print(' '.join(map(str,array)))
#         return
#
#
#     for num in range(1,n+1):
#         if array == [] or (num not in array and num > array[-1]):
#             array.append(num)
#             backtracking()
#             array.pop()
#
#
#
# n, m = map(int,input().split())
# array = []
#
# backtracking()

def dfs(start_idx):
    stack = graph[start_idx]
    visited[start_idx] = 1
    order = [start_idx]
    while stack:
        tmp = stack.pop()
        if visited[tmp] == 0:
            visited[tmp] = 1
            order.append(tmp)
            stack.extend(graph[tmp])
    return order


n,m,r = map(int,input().strip().split())
graph = [-1]+[[] for i in range(n)]
for _ in range(m):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1): graph[i].sort(reverse=True)
# print(graph)
visited = [-1] + [0] * n
visit_order = [0] * n
for idx,value in enumerate(dfs(r)):
    visit_order[value-1] = idx+1
print('\n'.join(map(str,visit_order)))

