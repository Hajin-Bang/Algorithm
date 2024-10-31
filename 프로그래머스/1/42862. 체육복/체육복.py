def solution(n, lost, reserve):
    new_lost = []
    new_reserve = []

    for stu in lost:
        if stu in reserve:
            reserve.remove(stu)  
        else:
            new_lost.append(stu)  


    new_reserve = reserve

    answer = n - len(new_lost)
    
    for i in sorted(new_lost):
        if i - 1 in new_reserve:  
            new_reserve.pop(new_reserve.index(i - 1))  
            answer += 1  
        elif i + 1 in new_reserve:  
            new_reserve.pop(new_reserve.index(i + 1)) 
            answer += 1  
        
    return answer 