# 피로도를 사용해서 던전을 탐험 
# 각 던전(dungeons) => [최소 필요 피로도, 소모 피로도]
# 유저의 현재 피로도 k로 하루에 탐험할 수 있는 최대 던전 수를 반환 

# dungeons [[80,20],[50,40],[30,10]] 
# 현재 피로도k 80
# [80,20] => 60
# [50,40] => 20
# [30,10] => 불가능

# [80,20] => 60
# [30,10] => 50
# [50,40] => 10 

# [30,10] => 70
# [50,40] => 30
# [80,20] => 불가능

# 만족시키는 순서같은건 없다. 그냥 모든 경우의 수를 탐험해야하나 ? 재귀? 
# 현재 피로도가 최소탐험피로도보다 큰가? => 탐험 => 현재피로도 - 소모 피로도 
## 반복
 
    
def solution(k, dungeons):
    is_explored = [0] * len(dungeons)
    return hehe(k, is_explored, dungeons, 0)

def hehe(k, is_explored, dungeons, count):
    max_count = count
    for i in range(len(dungeons)):
        if not is_explored[i]:
            if k >= dungeons[i][0]:
                is_explored[i] = 1
                left_k = k - dungeons[i][1]
                next_explore = hehe(left_k, is_explored, dungeons, count+1)
                max_count = max(max_count, next_explore)
                is_explored[i] = 0
                    
    return max_count