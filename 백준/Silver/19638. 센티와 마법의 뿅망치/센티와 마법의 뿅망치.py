import sys, heapq

N, H, T = map(int, sys.stdin.readline().split())
heights = [-int(sys.stdin.readline()) for i in range(N)]
heapq.heapify(heights)
count = 0 # 뿅망치 사용 횟수

# 뿅망치 제한 횟수가 0이 되기 전까지 반복
for i in range(T):
    max_height = -heapq.heappop(heights) # 가장 큰 키 꺼내기

    # 만약 제일 큰 키가 1이라면 다시 heights에 집어넣고 종료
    if max_height == 1 or max_height<H:
        heapq.heappush(heights, -max_height)
        break
    else: 
        half_height = max_height // 2
        heapq.heappush(heights, -half_height)
        count += 1

if -heights[0] < H:
    print("YES")
    print(count)
else:
    print("NO")
    print(-heights[0])