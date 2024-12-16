import sys

input = sys.stdin.readline

switch_num = int(input())
switch = list(map(int, input().split()))
student_num = int(input())
info = []
for _ in range(student_num):
    student, number = map(int, input().split())
    info.append((student, number))

for student, number in info:
    if student == 1:
        for i in range(number-1, switch_num, number):
            switch[i] = 1 - switch[i]

    elif student == 2:
        index = number - 1
        switch[index] = 1 - switch[index]

        left = index - 1
        right = index + 1

        while left >= 0 and right < switch_num and switch[left] == switch[right]:
                switch[left] = 1 - switch[left]
                switch[right] = 1 - switch[right]
                left -= 1
                right += 1


for i in range(0, switch_num, 20):  
    print(' '.join(map(str, switch[i:i+20])))