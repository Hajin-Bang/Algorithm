import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
bags = []

for _ in range(N):
    weight, price = map(int, input().split())
    jewels.append((weight, price))
for _ in range(K):
    bag_capacity = int(input())
    bags.append(bag_capacity)

jewels.sort()
bags.sort()

max_jewel_price = 0
jewel_index = 0
max_heap = [] # 담을 수 있는 무게의 보석들 중 가장 비싼 것을 담기 위함

# 각 가방에 대한 최대 가격의 보석을 선택
for bag_capacity in bags:
    while jewel_index < N and jewels[jewel_index][0] <= bag_capacity:
        heapq.heappush(max_heap, -jewels[jewel_index][1]) # 최대힙을 위해 음수로 저장
        jewel_index += 1

    # 담을 수 있는 무게의 보석들 중에 가장 비싼 것 담기
    if max_heap:
        max_jewel_price += -heapq.heappop(max_heap)

print(max_jewel_price)
