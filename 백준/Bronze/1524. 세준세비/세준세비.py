import sys, heapq

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    input() # 줄바꿈
    N, M = map(int, input().split()) 
    sejun = sorted(list(map(int, input().split()))) 
    sebi = sorted(list(map(int, input().split())))

    sejun_index = 0
    sebi_index = 0

    while sejun_index < N and sebi_index <M:
        # 세준이의 병사가 세비의 병ㅅ보다 약한 경우
        if sejun[sejun_index] < sebi[sebi_index]:
            sejun_index += 1 # 세준이의 병사 제거 (인덱스 증가)
        else: 
            sebi_index += 1 # 세비의 병사 제거
    
    # 세준이의 모든 병사가 제거된 경우 
    if sejun_index == N: # 세비의 승
        print("B")
    else: # 세준이의 승
        print("S")