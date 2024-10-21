# 특정 프로세스가 몇번째로 실행되는지 구하는 문제 
# 대기중인 프로세스를 꺼냄 
# 꺼낸 프로세스보다 우선순위가 더 높은게 있다면 꺼낸 것을 다시 집어넣음 
# 없다면 꺼낸 프로세스 실행
# 실행한 프로세스 종료
# 우선순위는 숫자가 클수록 높다

# [A,B,C,D] [2,1,3,2] 
# BCDA CDAB DAB AB B  
# C - D - A - B

# [1,1,9,1,1,1]  => 우선순위를 담을 배열
# ABCDEF BCDEFA CDEFAB DEFAB => 남은 프로세스를 담을 배열 
# C D E F A B  => 실행된 프로세스를 담을 배열
    
### 올바른 우선순위대로 프로세스를 넣는 것이 목표이다. ###

    
def solution(priorities, location):
    run = [] 
    remain = [] 
    
    for i in range(len(priorities)):
        remain.append((i, priorities[i])) 
        # [(0, 2), (1, 1), (2, 3), (3, 2)] (인덱스, 우선순위)
    
    while len(remain)>0:
        now_proccess = remain.pop(0)
        is_max = False
        for proccess in remain:
            if now_proccess[1] < proccess[1]:
                is_max = True
            
        if is_max:
            remain.append(now_proccess)
            
        else: 
            run.append(now_proccess) 
            if now_proccess[0] == location:  
                return len(run)
        
        
                