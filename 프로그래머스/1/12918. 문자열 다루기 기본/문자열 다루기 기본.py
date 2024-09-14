def solution(s):
    length = len(s)
    if length == 4 or length == 6:
        if s.isdigit():
            return True
        else: return False
    else: return False

