import sys 
from collections import deque

n = int(sys.stdin.readline().strip())
dq = deque()

for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        dq.append(command[1])
    elif command[0] == "pop":
        print(dq.popleft() if dq else -1)
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        print(1 if not dq else 0)
    elif command[0] == "front":
        print(dq[0] if dq else -1)
    elif command[0] == "back":
        print(dq[-1] if dq else -1)
