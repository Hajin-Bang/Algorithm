import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
line = deque() 

max_line_len = 0 
last_number = 0

for _ in range(n):
    student_info = list(map(int, input().split()))
    student_case = student_info[0]
    if len(student_info) >= 2: student_number = student_info[1]
    if student_case == 1:
        line.append(student_number)
    elif student_case == 2 and line:
        line.popleft()

    line_len = len(line)

    if line_len > max_line_len:
        max_line_len = line_len
        last_number = line[-1]
    elif line_len == max_line_len and line:
        last_number = min(line[-1], last_number)

print(max_line_len, last_number)