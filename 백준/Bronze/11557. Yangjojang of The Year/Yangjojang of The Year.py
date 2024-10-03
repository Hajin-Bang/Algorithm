import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    school_cnt = int(input())
    schools = [] # 학교별 소비량을 담을 리스트
    max_school = '' # 소비가 가장 많은 학교 이름
    
    # 각 학교의 소비량을 저장
    for _ in range(school_cnt):
        school_name, amount = input().split()
        schools.append((school_name, int(amount))) # [(학교명, 소비량)]
    
    schools.sort(key= lambda x: x[1]) # 소비량을 기준으로 오름차순 정렬
    max_school = schools[-1][0] # 맨 뒤에 정렬된 요소가 max인 학교
    print(max_school)