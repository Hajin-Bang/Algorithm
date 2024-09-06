A, B = map(list, input().split())

reversedA = "".join(map(str, reversed(A)))
reversedB = "".join(map(str, reversed(B)))

print(max(int(reversedA), int(reversedB)))