import sys
input = sys.stdin.read().splitlines()
N = int(input[0])

books = {}
for i in range(1, N+1):
    bookName = input[i]
    if bookName in books:
        books[bookName] += 1
    else: books[bookName] = 1

maxCount = max(books.values())

maxKeys = [key for key, value in books.items() if value == maxCount]
maxBook = min(key for key, value in books.items() if value == maxCount)

print(maxBook)