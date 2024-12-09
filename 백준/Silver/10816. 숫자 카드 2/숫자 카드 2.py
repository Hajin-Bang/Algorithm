import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
test_numbers = list(map(int, input().split()))

count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else: 
        count[number] = 1

result = []
for test in test_numbers:
    if test in count:
        result.append(count[test])
    else:
        result.append(0)

print(" ".join(map(str,result)))