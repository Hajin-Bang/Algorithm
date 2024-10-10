# 문제 분석
'''
- 배포되어야하는 작업 진도와 개발 속도가 주어질 때, 한번 배포할 때 몇개의 배포가 진행되는지를 출력하는 문제 
- progresses: 각 작업의 개발 진도
- speeds: 각 작업의 개발 속도 
- 각 기능은 진도가 100%일 때 반영될 수 있다. 
- 뒤의 기능이 먼저 개발되면, 앞의 기능이 다 배포될 때 같이 배포될 수 있다.
'''

# 의사 결정
'''
- 각 작업별 남은 일 수를 배열에 저장한다.
    - 작업 일수 계산: (100 - progress) / speed
    - 올림(ceil) 사용
- 배포하기 위해 쌓이는 작업의 수를 count한다. 
- 남은 일 수 리스트를 순회하면서 배포되는지 계산한다. 
    - 뒤의 수가 앞의 수보다 작으면 같이 배포 => count + 1
    - 뒤의 수가 앞의 수보다 크면 count에 담겨있는 작업 먼저 배포
        - count는 다시 1이 된다. 
'''
import math 

def solution(progresses, speeds):
    answer = []
    left_days = []
    
    for i in range(len(progresses)):
        left_day = math.ceil((100-progresses[i]) / speeds[i])
        left_days.append(left_day)
        
    prev = left_days[0]
    count = 1
    
    for i in range(1, len(left_days)):
        if left_days[i] <= prev:
            count += 1
        else:
            answer.append(count)
            count = 1
            prev = left_days[i]
    
    answer.append(count)
    return answer
            