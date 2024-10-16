# 문자열을 순회하면서, "("를 만나면 count+1
# ")"를 만나면 count-1 한다. 
# 만약 count가 음수가 되는 경우가 발생한다면, 올바르지 않은 괄호이다. 
    # 음수가 되는 경우는 시작이 ")"인 경우와 
    # ")"의 개수가 더 많은 경우 모두를 잡아줄 것이다.
# 마지막까지 순회한 뒤에는 count 값이 0인지 확인한다.
    # 0이라면 올바른 괄호
    # 0이 아니라면 괄호 개수가 맞지 않는 것이다. 


def solution(s):
    count = 0
    for i in range(len(s)):
        if (s[i] == "("): 
            count += 1 
        else:
            count -= 1
        if count < 0: # count 값이 음수가 되면 바로 return 반환
            return False
        
    return True if count == 0 else False
        