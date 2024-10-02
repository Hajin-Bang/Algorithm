import sys
input = sys.stdin.readline

k = int(input())
buildings = list(map(int, input().split()))

tree = [[] for _ in range(k)] # 레벨(깊이)별로 노드를 저장하기 위해 2차원 배열 생성

# nodes: 중앙순회결과 노드 리스트
# level: 현재 레벨 
def make_tree(nodes, level):
    # 노드 리스트가 비어있으면 종료
    if not nodes: 
        return 
    
    mid = len(nodes) // 2 # 빌딩 리스트의 중앙값
    tree[level].append(nodes[mid]) # 중앙값을 해당 level에 추가한다. 

    make_tree(nodes[:mid], level+1) # 왼쪽 서브트리 구성
    make_tree(nodes[mid+1:], level+1) # 오른쪽 서브트리 구성

make_tree(buildings, 0) # 트리 구성 함수를 호출해 레벨 0부터 트리 구성을 시작한다. 

# 각 레벨별로 노드를 출력한다. 
for i in range(k):
    print(' '.join(map(str,tree[i])))