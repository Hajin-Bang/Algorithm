import sys

input = sys.stdin.readline

n = int(input())

heights = []
building_counts = 0

for _ in range(n):
    height = list(map(int,input().split()))[1]
    
    # 현재 높이가 이전 높이보다 작으면 스택에서 제거
    while heights and heights[-1] > height:
        heights.pop()

    # 현재 높이가 이전 높이와 다르고 0이 아니면 새로운 건물로 판단
    if not heights or heights[-1] < height:
        if height != 0:
            building_counts += 1
        heights.append(height)

print(building_counts)