# 다리는 weight 이하까지의 무게를 견딜 수 있다.
# 다리에 완전히 오르지 않은 트럭의 무게는 무시 


# 다리길이: 2대 / 무게 제한:10kg
# [7,4,5,6]

## 다리 위에 있는 트럭 / 지난 트럭
## 시간 0초 => [] []
## 시간 1초 => [7] []
## 시간 2초 => [] [7]
## 시간 3초 => [4] [7]
## 시간 4초 => [4,5] [7]
## 시간 5초 => [5] [7,4]
## 시간 6초 => [] [7,4,5]
## 시간 7초 => [6] [7,4,5]
## 시간 8초 => [] [7,4,5,6]

# 트럭이 다리 위에 올라오면, 다음 트럭이 올라올 수 있는지 확인한다.
# 하나의 트럭을 완전히 건너도록 한다.  

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 시간: 몇 초 걸리는지
    bridge = [] # (다리를 건너는 트럭, )
    bridge_sum = 0 # 다리 위 무게 합
    
    # 대기하는 트럭이 있거나 / 다리 위에 트럭이 있을 때까지 반복
    while truck_weights or bridge: 
        answer += 1
        
        if len(bridge) == bridge_length:
            bridge_sum -= bridge.pop(0)
            

        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight: # 다리에 하나 더 올라갈 수 있는지 판단
                truck = truck_weights.pop(0) # 대기중인 트럭에서 하나 뺀다
                bridge.append(truck) # 다리에 추가
                bridge_sum += truck # 다리 위에 있는 트럭 무게 합에 더한다

            else: 
                bridge.append(0)
    
    
    return answer




def solution(bridge_length, weight, truck_weights):
    answer = 0 # 시간: 몇 초 걸리는지
    bridge = [] # [다리를 건너는 트럭, 남은 시간(남은 자리)]
    bridge_sum = 0 # 다리 위 무게 합
    
    # 대기하는 트럭이 있거나 / 다리 위에 트럭이 있을 때까지 반복
    while truck_weights or bridge: 
        answer += 1
        
        if bridge and bridge[0][1] == 0:  # 맨 앞의 트럭이 다리를 다 건넜을 경우
            bridge_sum -= bridge.pop(0)[0]
            

        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight: # 다리에 하나 더 올라갈 수 있는지 판단
                truck = truck_weights.pop(0) # 대기중인 트럭에서 하나 뺀다
                bridge.append([truck, bridge_length]) # 다리에 추가
                bridge_sum += truck # 다리 위에 있는 트럭 무게 합에 더한다

        for i in range(len(bridge)):
            bridge[i][1] -= 1
    
    return answer
