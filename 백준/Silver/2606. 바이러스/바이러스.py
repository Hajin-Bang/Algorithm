import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 0 # 연결된 컴퓨터 수를 저장

    while queue:
        cur_computer = queue.popleft()

        for next_computer in connections[cur_computer]:
            if not visited[next_computer]:
                queue.append(next_computer)
                visited[next_computer] = True
                count += 1
    return count

n = int(input())
m = int(input())
connections = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    computer_a, computer_b = map(int, input().split())
    connections[computer_a].append(computer_b)
    connections[computer_b].append(computer_a)
    
print(bfs(1))