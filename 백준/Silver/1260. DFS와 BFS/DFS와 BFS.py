import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M, V = map(int, input().split())

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        cur_v = queue.popleft()
        print(cur_v, end=' ')
        for neighbor in graph[cur_v]:
            if not visited[neighbor] :
                visited[neighbor] = True
                queue.append(neighbor)


graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph:
    graph[key].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(V,visited_dfs)
print()
bfs(V, visited_bfs)