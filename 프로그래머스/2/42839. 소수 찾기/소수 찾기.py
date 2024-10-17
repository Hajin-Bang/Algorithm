# 한자리 숫자가 적힌 종이 조각을 붙여 소수를 몇개 만들 수 있는지 구하기

# 숫자를 이어붙이고 소수인지 판단한다. 
# 숫자를 이어붙일 수 있는 방법 
    # 
# 이어붙인 숫자를 모두 판별하고, 소수인 것만 배열에 담는다. 
    # 수를 2부터 시작해서 계속 나눈다. 
from itertools import permutations
    
def solution(numbers):
    num_list = set()  # 중복을 피하기 위해 set 사용
    for i in range(1, len(numbers) + 1):
        perm = permutations(numbers, i)  # 순열로 가능한 모든 조합 찾기
        for p in perm:
            num_list.add(int(''.join(p)))  # 문자열을 숫자로 변환하여 set에 추가

    count = 0
    for num in num_list:
        if is_prime(num):  # 소수인 경우만 카운트
            count += 1

    return count
    
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
    