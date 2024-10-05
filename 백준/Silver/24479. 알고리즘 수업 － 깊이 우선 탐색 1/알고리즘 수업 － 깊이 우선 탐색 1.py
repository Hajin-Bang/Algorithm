import sys

input = sys.stdin.readline

def dfs(node):
    global order
    nodes_to_visited = [node] # 방문할 노드를 저장할 스택
    while nodes_to_visited:
        next_node = nodes_to_visited.pop() # 다음 방문할 노드
        if visited[next_node] == 0: # 미방문 노드라면
            visited[next_node] = order # 현재 노드의 방문 순서 기록
            order += 1 

            # 인접 노드를 스택에 추가 
            # 오름차순 방문을 위해 (가장 최근에 추가된 노드를 먼저 탐색하기 때문)
            for neighbor in reversed(graph[next_node]):
                if visited[neighbor] == 0: # 미방문 노드라면
                    nodes_to_visited.append(neighbor) # 스택에 추가
    


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 인접 리스트를 담을 2차원 배열
visited = [0] * (N + 1) # 방문 순서를 기록할 리스트
order = 1 # 방문 순서를 기록하기 위한 변수

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v) # u의 인접리스트에 v를 추가
    graph[v].append(u) # v의 인접리스트에 u를 추가

# 각 노드별 인접리스트를 오름차순으로 정렬한다. 
for node in graph:
    node.sort()

dfs(R) # 시작 지점부터 dfs를 수행한다.

# 각 노드의 방문 순서를 출력한다. 
for i in range(1, N+1):
    print(visited[i])