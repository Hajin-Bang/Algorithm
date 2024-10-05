import sys
from collections import deque

def bfs(node):
    global order
    queue = deque([node]) # 현재 노드를 큐에 추가
    visited[node] = order
    order += 1

    while queue:
        next_node = queue.popleft() # 가장 먼저 들어온 노드를 꺼냄
        
        # 현재 노드의 인접 노드들을 순회
        for neighbor in (graph[next_node]):
            if visited[neighbor] == 0: # 미방문 노드라면
                visited[neighbor] = order # 방문 순서 기록 
                order += 1 
                queue.append(neighbor) # 큐에 인접 노드 추가



input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
order = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    node.sort()


bfs(R)

for i in range(1,N+1):
    print(visited[i])