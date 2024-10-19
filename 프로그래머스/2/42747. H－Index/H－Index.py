# 




def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations), 0, -1):
        value = list(filter(lambda x: x>= i, citations))
        if len(value) >= i:
            return i
    return 0
        
        