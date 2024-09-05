def star(n, start, end):
    if n == 1:
        pattern[start][start] = 1
    else: 
        for i in range(start, end + 1):
            pattern[start][i] = 1
            pattern[end][i] = 1
            pattern[i][start] = 1
            pattern[i][end] = 1
        star(n - 1, start + 2, end - 2)

n = int(input())
size = 4 * (n - 1) + 1 
pattern = [[0] * size for i in range(size)]

star(n, 0, size - 1)

for row in pattern:
    for i in row:
        print("*" if i == 1 else ' ', end='')
    print()