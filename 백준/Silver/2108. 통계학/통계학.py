# 문제 분석
'''
- 주어진 수의 평균, 중앙값, 최빈값, 범위(최대-최소) 네가지 통계값을 구하는 문제
- 수의 개수 N(홀수)개
- 평균: 소수점 이하 첫째자리에서 반올림한 값
- 중앙값
- 최빈값: 여러개 있을 때는 최빈값 중 두번째로 작은 값
- 범위: 최댓값 - 최솟값
'''

# 의사 결정
'''
- 주어진 수들을 배열로 묶는다. 
- 각 통계값을 구하는 함수를 생성한다. 
- 평균을 구할 때 round 함수를 사용한다. 
- 중앙값을 구할 때 sort로 정렬한 뒤, len의 가운데 값을 출력한다. 
- 최빈값
    - 배열을 순회하면서, 각 요소가 등장한 횟수를 센다. 
    - 등장 횟수의 Max값을 찾는다.
    - 최빈값이 여러개라면, 빈도수에 따라 정렬한 뒤, 두번째 값을 출력한다. 
- 범위를 구할 때 max,min 함수를 사용한다. 
'''

import sys
from functools import reduce

input = sys.stdin.readline

N = int(input())
numbers = []

# 숫자를 모두 배열에 넣는다. 
for _ in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort() # 정렬을 미리 해둔다. [-2, 1, 2, 3, 5, 8]

# 평균
def average(numbers):
    sum = reduce(lambda x, y: x + y ,numbers)
    return round(sum / len(numbers))

# 중앙값
def mid(numbers):
    mid_idx = len(numbers) // 2
    return numbers[mid_idx]

# 최빈값
def most_frequent(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # 빈도수 기준 내림차순으로 정렬한 뒤
    # 동일한 값은 숫자를 오름차순으로 정렬한다. 
    sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0])) 
    max_frequency = sorted_frequency[0][1] # 최빈값

    modes = [] # 최빈값이 여러개인 경우에 담을 숫자들
    for num, freq in sorted_frequency:
        if freq == max_frequency: # 빈도수가 최빈값과 같다면
            modes.append(num) # 해당 숫자를 추가
    
    return modes[1] if len(modes) > 1 else modes[0] # 최빈값이 여러 개인 경우 두 번째로 작은 값 반환, 하나면 첫 번째 값 반환

# 범위 
def range(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num-min_num

print(average(numbers))
print(mid(numbers))
print(most_frequent(numbers))
print(range(numbers))