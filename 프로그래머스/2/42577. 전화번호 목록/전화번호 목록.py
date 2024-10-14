# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하는 문제
# 접두어인 경우가 있으면 false 없으면 true

# 의사 결정
'''
배열 안의 각 전화번호를 해시 테이블에 담는다. 
각 전화번호의 접두어가 될 수 있는 숫자를 탐색하면서, 그 숫자와 같은 수가 있는지 확인한다. 
'''

def solution(phone_book):
    phone_number = {}
    for number in phone_book:
        phone_number[number] = True;
        
    for number in phone_book:
        start = ""
        for i in range(len(number)-1): # 전화번호 전체를 제외한 나머지 경우를 순회한다. 
            start += number[i]
            if start in phone_number:
                return False
            
    return True 
        
    
        