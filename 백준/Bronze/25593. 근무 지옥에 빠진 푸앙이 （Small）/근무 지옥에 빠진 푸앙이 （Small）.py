import sys
input = sys.stdin.read()

lines = input.splitlines() # 줄 단위로 분리
N = int(lines[0])

workTime = {} # 근무자별 근무 시간을 저장할 딕셔너리 생성
time = [4, 6, 4, 10] # 시간대별 근무하는 시간 저장

for i in range(N): # 지정한 주만큼 순회
    for j in range(4): # 한 주에 4개의 줄 (근무시간대 4개)
        week = lines[1+i*4+j].split() # 해당하는 줄을 찾고 공백으로 나누기
        for k in range(len(week)):
            person = week[k]
            if person != '-': # '-'가 아닌 경우에만 처리
                if person not in workTime:
                    workTime[person] = 0 # 새 근무자 생성
                workTime[person] += time[j] # 근무 시간 추가

if not workTime:
    print("Yes")
else: 
    minHours = min(workTime.values()) # 최소 근무 시간
    maxHours = max(workTime.values()) # 최대 근무 시간

    # 최대 근무시간과 최소 근무시간의 차이가 12시간 이하인지 판단
    if maxHours - minHours <= 12:
        print("Yes")
    else: print("No")