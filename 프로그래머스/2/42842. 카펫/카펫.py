# 노란색 큰 격자를 만족시키는 가로 * 세로 조합을 먼저 찾고
# 그 경우가 갈색 수와 노란색 수를 모두 만족시키는지 확인한다. 
## 전체의 가로길이 = 노란색 가로길이 + 2
## 전체의 세로길이 = 노란색 세로길이 + 2
## 전체의 가로길이 * 전체의 세로길이 == 갈색 격자의 수 + 노란색 격자의 수


### yello가 24인 경우 
# 24,1 / 12,2 / 6,4 / 4,6

def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0: 
            width = (yellow//i) + 2
            length = i + 2
        
            if (width * length == brown + yellow):
                 return [width,length]