import sys

input = sys.stdin.readline

N = int(input())
words = []

for _ in range(N):
    word = input().strip()
    word_len = len(word)
    words.append((word, word_len))

# 중복을 제거한 words
# 단어의 길이를 기준으로 오름차순 정렬
# 같은 길이라면 단어를 사전순으로 정렬
sorted_words = sorted(set(words), key = lambda x: (x[1], x[0])) 

for word in sorted_words:
    print(word[0])
