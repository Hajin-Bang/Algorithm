# 문제 분석
'''
진영을 파괴하기 위해 진영한테 제일 빨리 도착하는 방법
진영한테 도착하지 못하는 경우는 -1
'''

# 의사 결정
'''
최단 거리를 구하는 문제이므로 BFS 활용
'''
from collections import deque

def bfs(start, maps, visited, directions, n, m):
    queue = deque([(start[0], start[1], 1)])
    visited[start[0]][start[1]] = 1
    
    while queue:
        x,y,count = queue.popleft()
        if x == n and y == m:
            return count
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 1 <= nx <= n and 1 <= ny <= m:
                if not visited[nx][ny] and maps[nx-1][ny-1] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count+1))
    return -1

    

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*(m+1) for _ in range(n+1)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    return bfs((1,1), maps, visited, directions, n, m) 
    