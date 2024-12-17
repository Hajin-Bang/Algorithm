import sys

input = sys.stdin.readline

test_case = int(input())

nums = []
for _ in range(test_case):
    num = int(input())
    nums.append(num)

max_num = max(nums)
dp = [0] * (max_num + 1)

for i in range(1, max_num+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    elif i >= 4:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in nums:
    print(dp[num])