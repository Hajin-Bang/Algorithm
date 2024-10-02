import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    sheep = 0
    wolves = 0
    queue = deque([(x,y)])
    visited[x][y] = 1 # 시작점 방문 처리

    # 현위치의 값이 늑대인지 양인지 판단
    if field[x][y] == 'k':
        sheep += 1
    elif field[x][y] == 'v':
        wolves += 1
    
    while queue:
        x, y = queue.popleft() 

        for dx, dy in directions:
            nx,ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and field[nx][ny] != '#':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

                    if field[nx][ny] == 'k':
                        sheep += 1
                    elif field[nx][ny] == 'v':
                        wolves += 1
    return sheep, wolves

r, c = map(int,input().split())
field = [list(input().strip()) for _ in range(r)] # 필드 배열을 2차원 리스트로 저장
visited = [[False] * c for _ in range(r)] # 방문 여부를 모두 false로 처리
directions = [(0,1), (0,-1), (1,0), (-1,0)] # 상하좌우 탐색을 위한 방향벡터
total_sheep = 0 # 살아남은 양의 수
total_wolves = 0 # 살아남은 늑대 수

surviving_sheep = 0 # 살아남은 양의 수
surviving_wolves = 0 # 살아남은 늑대의 수

# 필드 전체를 순회하며 BFS 탐색
for i in range(r):
    for j in range(c):
        # 미방문한 곳이고, 늑대나 양을 존재한다면
        if not visited[i][j] and field[i][j] in ['k', 'v']:
            sheep, wolves = bfs(i,j) # 영역을 탐색하고, 양과 늑대 수 반환값을 저장

            # 양과 늑대 수를 비교하여 살아남게되는 수 계산
            if sheep > wolves:
                surviving_sheep += sheep
            else: 
                surviving_wolves += wolves

print(surviving_sheep, surviving_wolves)
                

