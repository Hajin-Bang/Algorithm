import sys

input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    card_num = int(input())
    cards = list(input().split())
    
    word = cards[0]
    for i in range(1, card_num):
        if cards[i] <= word[0]:
            word = cards[i] + word
        else:
            word = word + cards[i]
    print(word)