import sys

while True: 
    line = sys.stdin.readline().rstrip()

    if line == '.': break

    stack = []
    balanced = True # 균형을 이루는지 판단

    # 문자열의 각 문자 순회
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                balanced = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break
    # balanced가 true이고 stack이 비어있지 않아야 균형 잡힌 문장
    if balanced and not stack:
        print("yes")
    else:
        print("no")