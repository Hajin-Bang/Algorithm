import sys

# 톱의 최대 높이를 찾기 위한 함수
def binary_search(arr, start, end):
    optimal_height = 0

    while start <= end:
        mid = (start + end) // 2 # 중간값을 톱의 높이로 설정
        total = 0 # 가져갈 수 있는 나무의 총 길이

        # 나무의 길이를 하나씩 순회하면서, 가져갈 수 있는 길이를 계산
        for tree in arr:
            if mid < tree:
                total += tree - mid

        if total == M: # 나무의 총 길이가 목표길이와 같다면
            return mid # 바로 높이를 반환
        
        elif total < M: # 나무의 총 길이가 목표 길이보다 작다면 
            end = mid - 1 # 높이를 더 줄여야하므로 범위의 끝을 중간보다 1작게 설정. 

        else: # 나무의 총 길이가 목표 길이보다 크다면
            optimal_height = mid # 현재 높이가 제일 적합할 수 있으므로 우선 저장
            start = mid + 1 # 높이를 높여봐야하므로 범위의 시작을 중간보다 1크게 설정

    return optimal_height

    

input = sys.stdin.readline
N, M = map(int, input().split())
tree_heights = list(map(int, input().split()))

print(binary_search(tree_heights, 0, max(tree_heights)))