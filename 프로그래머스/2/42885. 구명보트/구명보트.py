# 몸무게가 제일 많이 나가는 사람과 제일 적게 나가는 사람을 매칭한다. 
# 둘의 합한 무게가 limit보다 작으면 범위를 줄여나간다.  

def solution(people, limit):
    count = 0 
    start = 0 
    end = len(people) - 1
    people.sort()
    
    while(start<=end):
        if (people[start] + people[end] <= limit):
            start += 1
            end -= 1
            count += 1
        else: 
            end -= 1
            count += 1
	
    return count