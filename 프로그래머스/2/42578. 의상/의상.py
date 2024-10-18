def solution(clothes):
    hash = {} 
    for item in clothes:
        if item[1] in hash:
            hash[item[1]].append(item[0]) 
        else: 
            hash[item[1]] = [item[0]]
            
    combination = 1
    for key in hash:
        combination *= len(hash[key]) + 1
        
    return (combination - 1)
        
        