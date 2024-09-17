# 신청금액 d 예산 budget
# 최대 몇 개의 부서에 물품을 지원할 수 있는지
# d 오름차순으로 정렬하기
# budget에서 하나씩 빼기 
    # 뺄 때마다 budget과 다음 수 비교
    # budget이 같거나 더 클 때 
        # budget에서 값 빼기 
        # count 증가시키기


def solution(d, budget):
    dLen = len(d)
    count = 0
    d = sorted(d)
    for i in range(dLen):
        if d[i] <= budget:
            budget = budget - d[i]
            count += 1
    return count
    

    
    