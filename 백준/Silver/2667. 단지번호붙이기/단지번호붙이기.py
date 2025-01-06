import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
maps = []
for _ in range(N):
    line = list(map(int, input().strip()))
    maps.append(line)

visited = [[False]*N for _ in range(N)]
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True 
                queue.append((nx, ny))
                count += 1
    return count

counts = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and not visited[i][j]:
            counts.append(bfs(i,j))

counts.sort()
print(len(counts))
for count in counts:
    print(count)