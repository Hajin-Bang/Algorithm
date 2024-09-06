A, B = map(list, input().split())

reversedA = "".join(map(str, reversed(A)))
reversedB = "".join(map(str, reversed(B)))

if (int(reversedA) > int(reversedB)):
    print(reversedA)
else: print(reversedB)