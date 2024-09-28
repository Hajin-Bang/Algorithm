import sys, heapq

n = int(sys.stdin.readline().strip())
max_heap = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().strip().split()))

    # 충전하지 않고 아이들을 만난 경우
    # 힙이 비어있지 않으면 최댓값을, 비어있으면 -1을 출력한다. 
    if a[0] == 0:
        print(-heapq.heappop(max_heap) if max_heap else -1)
    else: 
        gifts_values = a[1:] # 충전한 선물 개수를 제외한 나머지 가치
        
        # 선물 가치를 힙에 넣는다.
        for value in gifts_values:
            heapq.heappush(max_heap, -value)