import sys, heapq

input = sys.stdin.readline
N = int(input())
dasom = int(input()) # 두번째 줄: 다솜이의 득표수
numbers = []


for i in range(N - 1):
    num = int(input())
    heapq.heappush(numbers, -num)

count = 0 
while numbers:
    num = -heapq.heappop(numbers)
    if num >= dasom:
        num -= 1
        dasom += 1
        count += 1
        heapq.heappush(numbers, -num)
    else: break

print(count)