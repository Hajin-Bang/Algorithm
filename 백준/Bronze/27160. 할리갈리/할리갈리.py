N = int(input())

STRAWBERRY = BANANA = LIME = PLUM = 0

for i in range(N):
    S, X = input().split()
    X = int(X)
    if (S == "STRAWBERRY"):
        STRAWBERRY += X
    elif (S == "BANANA"):
        BANANA += X
    elif (S == "LIME"):
        LIME += X
    elif (S == "PLUM"):
        PLUM += X

if (STRAWBERRY == 5 or BANANA == 5 or LIME == 5 or PLUM == 5):
    print("YES")
else: print("NO")