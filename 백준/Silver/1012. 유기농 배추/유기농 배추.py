import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x,y)]) # 현위치 x, 현위치 y
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0<= nx < M and 0<= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


test_case = int(input())

for _ in range(test_case):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)] # 그래프
    visited = [[False] * N for _ in range(M)] # 방문 여부 저장 배열
    directions = [(0,1), (1,0), (0,-1), (-1,0)] # 방향 벡터 

    # 배추가 있는 위치에 1 넣기
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    worm_count = 0
    for i in range(M):
        for j in range(N):
            # 1인 곳을 찾고, 인접한 1의 범위를 탐색하기
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                worm_count += 1

    print(worm_count)