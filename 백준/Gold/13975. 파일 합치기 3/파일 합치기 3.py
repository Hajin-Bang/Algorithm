import sys, heapq

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    k = int(input()) # 장 수
    files = list(map(int, input().split()))
    
    heapq.heapify(files) # 최소힙 생성 
    total_sum = 0 # 총 합

    # files의 크기가 1이 되기 전까지 반복
    while len(files) > 1:
        current_sum = heapq.heappop(files) + heapq.heappop(files) # 제일 작은 두 수의 합
        heapq.heappush(files, current_sum) # 합을 다시 힙에 추가
        total_sum += current_sum
        

    print(total_sum)