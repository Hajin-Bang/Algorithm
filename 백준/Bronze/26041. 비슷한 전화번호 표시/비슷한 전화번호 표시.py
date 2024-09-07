A = list(map(str, input().split()))
B = input()

result = []
for i in A:
    if i.startswith(B) and i != B:
        result.append(i)
print(len(result))