import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
directions = [(1, 0), (0, 1)]

def bfs(): 
    queue = deque([(0,0)])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        cell_value = board[x][y] # 칸에 쓰여져있는 수

        # 도착지점인 -1에 도달했을 때
        if cell_value == -1:
            print("HaruHaru")
            return 

        for dx, dy in directions:
            nx, ny = x + dx * cell_value, y + dy * cell_value

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    print("Hing")

bfs()