import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, target):
    queue = deque([(start, 0)]) # (현재 노드, 촌수)형태로 큐에 저장
    visited[start] = True # 시작 노드를 방문 처리

    # 큐가 빌 때까지 반복
    while queue:
        current, level = queue.popleft() # 현재 노드와 현재 촌수

        # 목표 노드에 도달하면 해당 촌수를 반환한다.
        if current == target:
            return level
        
        # 현재 노드에 연결된 모든 노드(사람)을 탐색
        for relative in family_tree[current]:
            if not visited[relative]: # 방문하지 않은 노드만 탐색
                visited[relative] = True
                queue.append((relative, level+1))

    return -1 # 목표 노드에 도달하지 못한 경우(관계를 찾지 못한 경우)

n = int(input())
person_a, person_b = map(int, input().split())
m = int(input())
family_tree = [[] for _ in range(n+1)] # 부모-자식 관계를 인접리스트로 담을 배열
visited = [False] * (n+1)

# m개의 줄을 순회하며 부모-자식 관계를 인접리스트로 담는다. 
for _ in range(m): 
    x, y = map(int, input().split())
    family_tree[x].append(y)
    family_tree[y].append(x)

print(bfs(person_a, person_b))