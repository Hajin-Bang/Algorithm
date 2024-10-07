import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_city):
    queue = deque([start_city])
    
    while queue:
        cur_city = queue.popleft()

        # 현재 도시에서 이동할 수 있는 모든 도시를 탐색한다. 
        for next_city in graph[cur_city]:
            if not visited[next_city]: # 아직 방문하지 않은 도시라면
                distance[next_city]= distance[cur_city] + 1 # 거리를 저장한다.
                visited[next_city] = True
                queue.append(next_city)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 도시별 방문 여부 표시
distance = [0] * (n+1) # 도시별 최단 거리 저장 
visited[x] = True # 출발 도시 방문 표시

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

bfs(x)

result = []

for city in range(1, n+1):
    if distance[city] == k:
        result.append(city)

if result:
    for city in sorted(result):
        print(city)
else: print(-1)

