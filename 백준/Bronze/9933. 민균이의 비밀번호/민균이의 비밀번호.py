import sys

N = int(sys.stdin.readline().strip())
words = {}
result = ""

for i in range(N):
    word = sys.stdin.readline().strip()
    words[word] = word[::-1] # 키:문자열 / 값:뒤집은 문자열 형태로 words에 저장
    if word[::-1] in words: # 뒤집은 문자가 words의 키에 있다면
        result = word
    elif word == word[::-1]:
        result = word

len_result = len(result)
print(len_result, result[len_result // 2] if len_result else " ")