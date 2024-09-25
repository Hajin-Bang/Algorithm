import sys

n = int(sys.stdin.readline().strip())
count = 0

for i in range(n):
    word = sys.stdin.readline().strip()
    stack = []
    
    for i in range(len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else: 
            stack.append(word[i])
    if not stack: 
        count += 1

print(count)