import sys

input = sys.stdin.readline

N = int(input())
Xi = list(map(int, input().split()))
sorted_Xi = sorted(set(Xi)) # 중복을 없애고 오름차순으로 정렬한 Xi

Xi_index = {} # {배열값: 인덱스} 형태로 저장할 딕셔너리
index = 0 # 딕셔너리 값에 넣을 인덱스

# Xi의 각 요소를 순회 
for x in sorted_Xi:
    Xi_index[x] = index # {배열값: 인덱스}로 저장
    index += 1

compressed_Xi = [Xi_index[x] for x in Xi]

print(' '.join(map(str, compressed_Xi)))