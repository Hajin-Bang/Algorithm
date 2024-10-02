import sys

# formed_number: 현재까지 이어붙인 문자열
def dfs(x, y, formed_number):
    # 이동 횟수가 6번이면(만들어진 숫자 길이가 6이면) 숫자를 저장하고 종료
    if len(formed_number) == 6:
        six_digit_numbers.add(formed_number)
        return

    # 네 방향으로 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0<= ny < 5:
            dfs(nx, ny, formed_number + numbers[nx][ny]) # 이동한 위치의 숫자를 이어붙이고 재귀 호출


numbers = [sys.stdin.readline().split() for _ in range(5)] # 각 칸에 해당하는 숫자를 행별로 리스트에 담는다. 
directions = [(1,0), (0,1), (-1,0), (0,-1)] # 방향 벡터 설정
six_digit_numbers = set() # 만들어진 숫자들을 중복 없이 저장


for i in range(5):
    for j in range(5):
        dfs(i, j, numbers[i][j]) # (i,j)에서 시작

print(len(six_digit_numbers))