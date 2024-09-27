import sys
import heapq

n = int(sys.stdin.readline().strip())
min_heap = []

for i in range(n):
    num = list(map(int ,sys.stdin.readline().strip().split(" ")))
    for j in range(n):
        if len(min_heap) < n:
            heapq.heappush(min_heap, num[j])
        elif min_heap[0] < num[j]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num[j])

print(min_heap[0])