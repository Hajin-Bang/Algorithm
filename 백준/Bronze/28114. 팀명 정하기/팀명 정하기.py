import sys
input = sys.stdin.readline

students = []
first_team_name = ''
second_team_name = ''

for _ in range(3):
    solved_count, year, last_name = input().split()
    students.append((int(solved_count), int(year) % 100, last_name))

# 입학연도를 기준으로 팀명 만들기
students.sort(key= lambda x: x[1]) # 입학연도 기준으로 오름차순 정렬
first_team_name = ''.join(str(student[1]) for student in students)

# 해결한 문제 수 기준으로 팀명 만들기 
students.sort(key= lambda x: x[0], reverse=True) # 해결한 문제가 많은 순으로 정렬
second_team_name = ''.join(student[2][0] for student in students)

print(first_team_name)
print(second_team_name)