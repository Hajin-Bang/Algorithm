import sys
from collections import deque

input = sys.stdin.readline

def bfs(x): 
    queue = deque([x])
    visited[x] = True
    while queue:
        cur_x = queue.popleft()
        for neighbor in graph[cur_x]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

N, M = map(int, input().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

connected_components = 0
for x in range(1, N+1):
    if not visited[x]:
        bfs(x)
        connected_components += 1
    
print(connected_components)