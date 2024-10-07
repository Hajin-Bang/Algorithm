
import sys
from collections import deque

input = sys.stdin.readline

def bfs(lake_position, barn_position):
    queue = deque([(lake_position[0], lake_position[1], 0)]) # (x, y, 거리)
    visited[lake_position[0]][lake_position[1]] = True # 호수 위치 방문 체크

    while queue:
        x, y, distance = queue.popleft()

        # 헛간에 도달하면 경로 길이를 반환한다. 
        if (x, y) == barn_position:
            return distance - 1 # 소가 놓이는 빈칸의 수를 반환하기 위해 1을 뺀다.
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 그리드 범위 내에 있고
            # 아직 방문하지 않았고
            # 바위가 아닌 경우
            if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and grid[nx][ny] != 'R':
                visited[nx][ny] = True # 방문처리
                queue.append((nx, ny, distance + 1))


grid = [input().strip() for _ in range(10)] 
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*10 for _ in range(10)]
lake_position = (0,0) # 호수의 위치
barn_position = (0,0) # 헛간의 위치 

# 호수와 헛간의 위치 찾기
for i in range(10):
    for j in range(10):
        if grid[i][j] == "L":
            lake_position = (i,j)
        elif grid[i][j] == "B":
            barn_position = (i,j)

print(bfs(lake_position, barn_position))