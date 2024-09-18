def solution(n):
    strN = str(n)
    return int(''.join(sorted(strN, reverse=True)))




# 문자열로 바꿈
# 문자열 정렬 ==> 리스트 형태로 반환됨
# join으로 다시 합침 
# 합친 문자열을 int형으로 반환