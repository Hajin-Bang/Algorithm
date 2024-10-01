import sys

input = sys.stdin.readline

n, k = map(int, input().split()) 
experience = list(map(int, input().split()))
experience.sort()

total_experience = 0
active_stones = 0

for exp in experience:
    total_experience += exp * active_stones # 현재 활성화된 아케인스톤 수에 따라 경험치 추가

    if active_stones < k:
        active_stones += 1

print(total_experience)