import sys

# 톱의 최대 높이를 찾기 위한 함수
def binary_search(arr, start, end):
    result = 0 # 톱의 최적 높이를 저장하는 변수

    while start <= end:
        mid = (start + end) // 2 # 중간값을 톱의 높이로 설정
        total = 0 # 가져갈 수 있는 나무의 총 길이

        # 나무의 길이를 하나씩 순회하면서, 가져갈 수 있는 길이를 계산
        for tree in arr:
            if mid < tree:
                total += tree - mid

        # 총 나무의 길이가 목표치 M보다 작으면 
        if total < M:
            end = mid - 1 # 톱의 높이를 낮춤
        else: # 목표치보다 같거나 크면 (mid로 충분히 목표를 달성할 수 있다는 뜻)
            result = mid
            start = mid + 1 # 탐색의 범위를 높여본다.(톱의 높이를 높임)
    return result

    

input = sys.stdin.readline
N, M = map(int, input().split())
tree_heights = list(map(int, input().split()))



print(binary_search(tree_heights, 0, max(tree_heights)))