import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])

STRAWBERRY = BANANA = LIME = PLUM = 0

for i in range(1, N + 1):
    S, X = data[i].split()
    X = int(X)
    if S == "STRAWBERRY":
        STRAWBERRY += X
    elif S == "BANANA":
        BANANA += X
    elif S == "LIME":
        LIME += X
    elif S == "PLUM":
        PLUM += X

# 한 번만 모든 과일의 개수를 비교하는 최적화
if STRAWBERRY == 5 or BANANA == 5 or LIME == 5 or PLUM == 5:
    print("YES")
else:
    print("NO")