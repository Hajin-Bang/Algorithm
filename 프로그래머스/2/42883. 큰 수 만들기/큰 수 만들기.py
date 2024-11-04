# (수의 길이 - k)의 길이로 만들 수 있는 모든 조합을 구한다. 
# 조합 중 최댓값을 출력한다. 
# 헐 시간이 너무 마니 걸림 
# 수를 만들면서 동시에 값을 비교해야 한다. 
# "4321", k = 1

def solution(number, k):
    answer = []
    length = 0
    
    for num in number:
        while length < k:
            if answer and answer[-1] < num:
                answer.pop()
                length += 1
            else: 
                break
        answer.append(num)
                      
    if length < k:
        answer = answer[:-k] # 뒤에서부터 제거 
        
            
    return ''.join(answer)
    
    