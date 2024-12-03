import sys

input = sys.stdin.readline

num = int(input())

scores = [0]
dp = [0] * (num + 1)

for _ in range(num):
    score = int(input())
    scores.append(score)

for i in range(1, num+1):
    if i == 1:
        dp[i] = scores[i]
    elif i == 2:
        dp[i] = scores[1] + scores[2]
    elif i>=3:
        dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i-1]+scores[i]) 

print(dp[num])