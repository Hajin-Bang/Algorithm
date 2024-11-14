# A B 중 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다
# 주고 받은 수가 같거나 기록이 없으면 
    # 선물지수가 작은 사람 -> 선물 지수가 더 큰 사람 
    # 선물지수가 같다면 다음달에 선물을 주고받지 않는다  
# 선물 지수: 자신이 준 선물 수 - 받은 선물 수

# friends: 친구들의 이름 목록
# gifts: 친구들이 주고받은 선물 기록 

# 다음 달에 가장 많은 선물을 받는 찬구가 받을 선물의 수 return

##문제 풀이 
# 모두의 선물 지수를 계산해야한다. 
# dictionary에 사람: [준 선물 수, 받은 선물 수, 선물지수] 로 저장
    # {muzi: [2, 5, -3]}
    


def solution(friends, gifts):
    list = {}
    give_count = {}
    
    for friend in friends:
        list[friend] = [0,0,0]
        give_count[friend] = {}
        for other in friends:
            if friend != other:
                give_count[friend][other] = 0
        
    for gift in gifts:
        giver, receiver = gift.split() 
        
        list[giver][0] += 1
        list[receiver][1] += 1
        give_count[giver][receiver] += 1
        
    for friend in list: # 선물지수 계산
        list[friend][2] = list[friend][0] - list[friend][1]
    
    next = {} # 다음 달 선물 
    for friend in friends: 
        next[friend] = 0
        
    # 모든 친구 쌍 비교 
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            A, B = friends[i], friends[j] 
            A_to_B = give_count[A][B]
            B_to_A = give_count[B][A]
            
                    
            if A_to_B > B_to_A: # 더 많이 선물 준사람 비교
                next[A] += 1
            elif A_to_B < B_to_A: 
                next[B] += 1
            else: # 선물 준 횟수가 같거나 기록이 없으면
                if list[A][2] > list[B][2]: # 선물 지수 비교
                    next[A] += 1
                elif list[A][2] < list[B][2]:
                    next[B] += 1
                elif list[A][2] == list[B][2]:  
                    continue
    return max(next.values())
    
    
    