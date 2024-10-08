import sys
from collections import deque

input = sys.stdin.readline

def bfs(N, K):
    queue = deque([(N, 0)]) # 수빈이의 시작 위치, 걸린 시간
    visited[N] = True # 시작 위치 방문 표시

    while queue:
        cur_pos, count = queue.popleft()
        next_positions = [cur_pos-1, cur_pos+1, 2*cur_pos] # 다음 위치의 후보들

        # K에 도달하면 바로 반환
        if cur_pos == K:
            return count 
        
        # 다음 위치의 후보들을 순환
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, count+1))

N, K = map(int,input().split())
visited = [False] * 100001

print(bfs(N, K))