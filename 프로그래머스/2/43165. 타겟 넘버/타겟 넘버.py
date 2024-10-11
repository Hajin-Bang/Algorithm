# 문제 분석
'''
- 주어진 number 배열의 요소를 더하거나 빼서 타겟 넘버를 만들어야 한다. 
- 순서는 바꿀 수 없다. 
- 만들 수 있는 방법의 수를 출력한다. 
'''

# 의사 결정
'''
- 모든 조합을(경우의 수) 다 탐색해서 맞는 값만 골라내야한다. 
    - 각 숫자는 더하거나 빼는 두가지 경우의 수가 있다. 
- 모든 경우의 수를 다 탐색하기 위해 dfs로 구현한다. 

- number = [4, 1, 2, 1]
- 4는 +4, -4
- 1은 +1, -1
- 2는 +2, -2
- 1은 +1, -1 
'''

def dfs(numbers, target, result_sum, depth):
    global result 
    
    if depth == len(numbers): # 끝까지 내려갔을 때
        if result_sum == target:
            result += 1
        return 
    
    # 더하는 경우의 수, 빼는 경우의 수 
    dfs(numbers, target, result_sum + numbers[depth], depth+1)
    dfs(numbers, target, result_sum - numbers[depth], depth+1)
    
def solution(numbers, target):
    global result
    result = 0
    dfs(numbers, target, 0, 0)
    return result 