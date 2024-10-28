def dfs(node, visited, graph):
    visited[node] = 1
    count = 1 # 개수 세기 
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited, graph)
    return count
            

def solution(n, wires):
    graph = {}
    for i, j in wires:
        if i not in graph:
            graph[i] = []
        if j not in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)

    answer = []
    
    for i,j in wires:
        graph[i].remove(j)
        graph[j].remove(i)
        visited = [0] * (n+1)
        
        
        
        ## 두 그래프의 크기 차이 계산
        a_tree_size = dfs(i,visited,graph)
        b_tree_size = n - a_tree_size
        
        if a_tree_size >= b_tree_size:
            difference = a_tree_size - b_tree_size
        else: difference = b_tree_size - a_tree_size
        
        graph[i].append(j)
        graph[j].append(i)
        
        answer.append(difference) 
        
    return min(answer)