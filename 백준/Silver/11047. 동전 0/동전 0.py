
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
count = 0
for coin in coins:
    value = K // coin
    count += value
    K %= coin

    if K == 0:
        break
    
print(count)