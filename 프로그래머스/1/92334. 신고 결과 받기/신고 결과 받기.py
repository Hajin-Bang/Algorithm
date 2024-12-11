'''
한 번에 한명의 유저 신고
동일한 유저에 대한 신고는 1회로 처리
k번 이상 신고된 유저는 게시판 이용이 정지, 신고한 유저들에게 정지 사실을 메일로 발송
'''

'''
[muzi frodo apeach neo] 
k=2: 2번 이상 신고당하면 이용 정지


* 각 유저별 신고한 내역을 저장하는 객체
muzi: 2
frodo: 1
apeach: 1
neo: 0

* 각 유저별 신고당한 내역을 저장하는 객체
muzi: 1, [apeach]
frodo: 2, [muzi, apeach]
apeach: 0, []
neo: 2, [frodo, muzi]


각 유저별로 처리 결과 메일을 받은 횟수
'''


def solution(id_list, report, k):
    report = list(set(report))
    
    report_list = {id: [] for id in id_list} # 신고한 내역
    reported_count = {id: [] for id in id_list} # 신고 당한 내역
    
    for i in report:
        reporter = i.split()[0]
        reported = i.split()[1]
        report_list[reporter].append(reported)  
        reported_count[reported].append(reporter)  
    
    stopped_users = []
    for reported in reported_count:
        if len(reported_count[reported]) >= k:
            stopped_users.append(reported)
    
    result = []
    for report in report_list:
        count = 0
        for user in stopped_users:
            if user in report_list[report]:
                count += 1
        result.append(count)
    
    return result


'''
report_list = { 
                "muzi":["neo","frodo"],
                "frodo":["neo"],
                "apeach":["frodo","muzi"],
                "neo":[] 
                }
                
reported_count = {
                    "muzi":["apeach"],
                    "frodo":["apeach","muzi"],
                    "apeach":[],
                    "neo":["frodo","muzi"]
                }
                
stopped_users = ["frodo","neo"]
'''