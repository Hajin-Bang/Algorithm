import sys

input = sys.stdin.readline

stu_num = int(input())
stu_info = {}
for i in range(stu_num):    
    stu_info[i] = list(map(int, input().split())) 

count = [0] * stu_num

for key in stu_info:
    for other in stu_info:
        if key == other:
            continue
        for i in range(5):
            if stu_info[key][i] == stu_info[other][i]:
                count[key] += 1
                break

max_key = count.index(max(count))
print(max_key+1)