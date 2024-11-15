def solution(line):
    star_list = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            
            if A*D - B*C == 0:
                continue
            
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            
            if x % 1 == 0 and y % 1 == 0: 
                star_list.append([int(x),int(y)])
    
    # 영역 구하기
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    for i in star_list:
        x, y = i
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
            
    # 전체 크기 계산
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    result = []
    
    for _ in range(height):
        row = []  
        for _ in range(width):
            row.append('.')  
        result.append(row) 
    
    for x, y in star_list:
        row = max_y - y
        col = x - min_x
        result[row][col] = '*'
    
    final_result =[]
    for row in result:
        final_result.append(''.join(row))

    return final_result

    