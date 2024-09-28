import sys, heapq

N = int(sys.stdin.readline().strip())

min_heap = []

for i in range(N):
    number_X = int(sys.stdin.readline().strip())
    if number_X == 0: 
        if min_heap: print(heapq.heappop(min_heap))
        else: print(0)
    else: 
        heapq.heappush(min_heap, number_X)