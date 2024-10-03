import sys

input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split()))) # 티켓 번호들을 리스트에 담고 오름차순 정렬
smallest_missing = 1 # 누락된 최소 숫자를 저장할 변수 - 1부터 시작해서 비교

# 팔린 티켓 번호들을 순회한다. 
for num in numbers:
    # 현재 숫자가 smallest_missing보다 작으면 누락된 숫자를 찾은 것
    if smallest_missing < num:
        break
    # 현재 숫자가 smallest_missing보다 작으면
    elif smallest_missing == num:
        smallest_missing += 1  # +1시키고 다음 값과 비교

print(smallest_missing)
