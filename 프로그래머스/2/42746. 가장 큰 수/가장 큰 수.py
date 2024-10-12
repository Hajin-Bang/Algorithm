from functools import cmp_to_key

# 두 숫자를 이어붙여 더 큰 값이 앞에 오도록 비교하는 함수
def compare(a, b):
    if a + b > b + a:
        return -1  # a가 앞에 와야 함
    elif a + b < b + a:
        return 1   # b가 앞에 와야 함
    else:
        return 0   # 둘의 순서는 상관없음

def solution(numbers):
    # 1. 숫자를 문자열로 변환
    numbers_str = list(map(str, numbers))

    # 2. cmp_to_key를 사용하여 두 숫자를 비교하는 함수를 기반으로 정렬
    sorted_numbers = sorted(numbers_str, key=cmp_to_key(compare))

    # 3. 정렬된 숫자들을 이어붙임
    result = ''.join(sorted_numbers)

    # 4. 만약 결과가 '0'으로 시작하면 '0' 반환
    return result if result[0] != '0' else '0'
