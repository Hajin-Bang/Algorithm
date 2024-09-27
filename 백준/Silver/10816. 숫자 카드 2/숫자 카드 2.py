import sys

input = sys.stdin.read

data = input().split()

N = int(data[0])
cards = map(int, data[1:N+1])

M = int(data[N+1])
queries = map(int, data[N+2:])

card_count = {}
result = []

for card in cards: 
    if card in card_count:
        card_count[card] += 1
    else: 
        card_count[card] = 1

for query in queries:
    if query in card_count:
        result.append(str(card_count[query]))
    else:
        result.append('0')
    
print(' '.join(result))