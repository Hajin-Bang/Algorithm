# 문제 분석
'''
- 모든 음식의 스코빌 지수를 K 이상으로 만들어야한다.
- 가장 낮은 두개의 음식을 섞는다. 
- 섞어야하는 최소 횟수를 출력한다. 
'''

# 의사 결정
'''
- heapify 사용 (최소힙)
- 가장 작은 두 값을 차례로 꺼내서 스코빌 지수를 계산: heappop
- 계산한 스코빌 지수를 heap에 추가: heappush
- 가장 작은 수의 스코빌 지수가 K를 넘으면 성공 => count한 횟수 반환]
- 더이상 합칠 스코빌 개수가 없는데 K를 넘지 못한다면, -1를 반환해야한다. 
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        heapq.heappush(scoville, mix)
        count += 1
        
    return count
        
        
    
        
    