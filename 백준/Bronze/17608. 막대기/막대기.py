import sys

n = int(sys.stdin.readline().strip())
stack = list(map(int, (line.strip() for line in sys.stdin.readlines()))) # 각 줄을 정수로 변환하여 stack에 저장

last = stack.pop()
count = 1 # 마지막 값 포함

for i in range(len(stack)):
    if last < stack[-1]:
        last = stack.pop()
        count += 1
    else: stack.pop()

print(count)