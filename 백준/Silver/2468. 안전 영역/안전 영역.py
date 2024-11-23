import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

def dfs(x,y,height):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and heights[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

heights = []
max_height = 0
min_height = 100
for _ in range(N):
    line = list(map(int, input().split()))
    max_height = max(max(line), max_height)
    min_height = min(min(line), min_height)
    heights.append(line)
directions = [(1,0),(0,1),(-1,0),(0,-1)]

max_areas = 0
for height in range(min_height-1, max_height):
    visited = [[False] * N for _ in range(N)]
    areas = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and heights[i][j] > height:
                dfs(i, j, height)
                areas += 1
    max_areas = max(max_areas, areas)

print(max_areas)