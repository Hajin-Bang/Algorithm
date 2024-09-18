# 숫자를 문자형으로 변환 
# 각 자릿수 더함
# 만약 x % 자릿수 합 == 0 이라면 true 반환

def solution(x):
    sumNum = sum(map(int, str(x)))
    if x % sumNum == 0:
        return True
    else: return False
    