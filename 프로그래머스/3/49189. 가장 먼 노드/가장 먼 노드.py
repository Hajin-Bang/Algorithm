from collections import deque

def bfs(graph, distances, start):
    queue = deque([start])
    distances[start] = 1
    
    while queue: 
        current = queue.popleft()
        for i in graph[current]:
            if distances[i] == 0:
                distances[i] = distances[current] + 1
                queue.append(i)
                
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    distances = [0] * (n+1)
    bfs(graph, distances, 1)

    max_distance = max(distances)
    answer = []
    for i in distances:
        if i == max_distance:
            answer.append(i)
    
    return len(answer)
    
    
    