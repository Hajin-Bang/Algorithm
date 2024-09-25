import sys 
from collections import deque

n = int(sys.stdin.readline().strip())
dq = deque()

for i in range(n):
    info = sys.stdin.readline().split()

    if info[0] == 'push_front':
        dq.appendleft(info[1])
    elif info[0] == 'push_back':
        dq.append(info[1])
    elif info[0] == 'pop_front':
        if len(dq) == 0: print(-1)
        else: 
            print(dq[0])
            dq.popleft()
    elif info[0] == 'pop_back':
        if len(dq) == 0: print(-1)
        else:
            print(dq[len(dq) - 1])
            dq.pop()
    elif info[0] == 'size':
        print(len(dq))
    elif info[0] == 'empty':
        if len(dq) == 0: print(1)
        else: print(0)
    elif info[0] == 'front':
        if len(dq) == 0: print(-1)
        else: print(dq[0])
    elif info[0] == 'back':
        if len(dq) == 0: print(-1)
        else: print(dq[len(dq)-1])