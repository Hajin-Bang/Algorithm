import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    applicants = []

    for _ in range(N):
        document_rank, interview_rank = map(int, input().split())
        applicants.append((document_rank, interview_rank))

    applicants.sort(key=lambda x: x[0]) # 서류 성적을 기준으로 정렬

    selected_count = 1 # 첫번째 지원자(서류 심사 1등)는 무조건 선발 
    min_interview_rank = applicants[0][1] # 첫번째 지원자의 면접 순위 

    for i in range(1,N):
        if applicants[i][1] < min_interview_rank:
            selected_count += 1
            min_interview_rank = applicants[i][1]

    print(selected_count)