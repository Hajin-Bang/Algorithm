import sys

input = sys.stdin.readline
N, M = map(int, input().split())

songs = {}

# 노래 목록 저장
for _ in range(N):
    song = input().split()
    name = song[1]
    melody = ''.join(song[2:5])

    if melody not in songs:
        songs[melody] = []
    songs[melody].append(name) # 존재하는 개수만큼 리스트에 모두 담음
    
# 노래 맞히기
for _ in range(M):
    guessed_song = ''.join(input().split())
    
    if guessed_song in songs:
        if len(songs[guessed_song]) == 1:
            print(songs[guessed_song][0]) # 노래 제목 출력
        else:
            print('?')
    else: print('!')

