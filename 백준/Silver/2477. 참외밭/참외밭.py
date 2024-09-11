import sys
input = sys.stdin.readline

melon = int(input())

arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))

maxWidth = [0, 0]
maxHeight = [0, 0]
for i in range(6):
    if (arr[i][0] == 1 or arr[i][0] == 2) and (arr[i][1] > maxWidth[1]): # 가로
        maxWidth = [i, arr[i][1]]
    elif (arr[i][0] == 3 or arr[i][0] == 4) and (arr[i][1] > maxHeight[1]): # 세로
        maxHeight = [i, arr[i][1]]

minWidth = abs(arr[(maxHeight[0]+1)%6][1]-arr[(maxHeight[0]-1)%6][1])
minHeight = abs(arr[(maxWidth[0]-1)%6][1]-arr[(maxWidth[0]+1)%6][1])

print(melon*(maxWidth[1]*maxHeight[1]-minWidth*minHeight))