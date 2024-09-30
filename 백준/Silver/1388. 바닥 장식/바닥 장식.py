import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue: 
        x, y = queue.popleft()
        if floor[x][y] == '-':
            if y + 1 < m and not visited[x][y + 1] and floor[x][y + 1] == '-':
                visited[x][y+1] = 1
                queue.append((x, y+1))
        elif floor[x][y] == '|':
            if x + 1 < n and not visited[x+1][y] and floor[x+1][y] == '|':
                visited[x+1][y] = 1
                queue.append((x+1, y))



n,m = map(int, input().split())
floor = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)] # 방문 여부를 모두 false로 처리
count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)