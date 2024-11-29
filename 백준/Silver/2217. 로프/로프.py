import sys

input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()

weights = []
rope_num = 1
for rope in ropes:
    total_weight = rope * (N-(rope_num - 1))
    weights.append(total_weight)
    rope_num += 1

print(max(weights))