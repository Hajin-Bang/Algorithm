import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

def bfs(l, start, end):
    queue = deque([(start[0], start[1], 0)]) # (현재 x위치, 현재 y위치, 이동횟수)
    visited[start[0]][start[1]] = True

    while queue:
        cur_x, cur_y, move_count = queue.popleft()

        # 목표 위치에 도달한 경우 이동 횟수를 반환한다. 
        if (cur_x, cur_y) == (end[0], end[1]):
            return move_count
        
        # 모든 이동 방향을 탐색한다. 
        for direction in directions:
            next_x = cur_x + direction[0]
            next_y = cur_y + direction[1]

            if 0 <= next_x < l and 0 <= next_y < l and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, move_count+1))


for _ in range(test_case):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[False]*l for _ in range(l)]
    directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    
    print(bfs(l, start, end))
