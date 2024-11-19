import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
ground = []
for _ in range(N):
    line = input().strip()
    ground.append(list(line))
visited = [[False] * M for _ in range(N)]
lr_directions = [(0,1),(0,-1)]
ud_directions = [(1,0),(-1,0)]
board = 0

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        if ground[x][y] == '-':
            for dx, dy in lr_directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ground[nx][ny] == '-': 
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        elif ground[x][y] == '|':
            for dx, dy in ud_directions:  
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ground[nx][ny] == '|':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i,j)
            board += 1

print(board)