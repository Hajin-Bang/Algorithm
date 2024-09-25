import sys
from collections import deque

n = int(sys.stdin.readline())

result = deque()
stack = []

# 2 ~ N번째 줄을 순회
for i in range(n):
    info = sys.stdin.readline().split() # 각 줄을 공백으로 분리 => ["1", "a"]

    # 숫자(1,2,3)에 따른 조건부 실행
    if info[0] == "1":
        result.append(info[1])
        stack.append('back') # stack에 기록 
    elif info[0] == "2":
        result.appendleft(info[1])
        stack.append('front') # stack에 기록 
    elif info[0] == "3":
        if stack: 
            last = stack.pop() # 맨 마지막에 추가된 기록 꺼내기
            # 마지막 기록이 앞에 추가된 문자인지 뒤에 추가된 문자인지에 따라 조건부 실행
            if last == "front": 
                result.popleft() # 맨 앞 제거
            else: 
                result.pop() # 맨 뒤 제거

if result:
    print(''.join(result))
else:
    print(0)