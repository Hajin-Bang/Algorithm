import sys
input = sys.stdin.readline

# dfx 탐색을 위한 함수
def dfs(x, y):
    visited[x][y] = 1 # 방문 처리 
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n: # 필드 범위 내에 있는지 확인
            if not visited[nx][ny] and field[nx][ny] == '#': # 미방문 풀(#)인 경우
                dfs(nx, ny) # 인접한 풀을 탐색

m, n = map(int, input().split())
field = [list(input().strip()) for _ in range(m)] # 필드 배열을 (각 줄별) 2차원 리스트로 저장
visited = [[0] * n for _ in range(m)] # 방문 여부를 모두 false로 처리
directions = [(0,1), (0,-1), (1,0), (-1,0)] # 상하좌우 탐색을 위한 방향 벡터
grass_area_count = 0 # 연결된 풀 영역의 개수

# 필드 전체를 순회하며 DFS 탐색
for i in range(m):
    for j in range(n):
        if not visited[i][j] and field[i][j] == '#': # 미방문 풀을 발견하면
            dfs(i, j) # 해당 영역을 탐색한다.
            grass_area_count += 1

print(grass_area_count)