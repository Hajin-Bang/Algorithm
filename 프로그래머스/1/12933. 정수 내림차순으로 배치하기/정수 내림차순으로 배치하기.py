def solution(n):
    strN = str(n)
    return int(''.join(sorted(strN, reverse=True)))