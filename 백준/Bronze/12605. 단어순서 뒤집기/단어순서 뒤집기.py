import sys

n = int(sys.stdin.readline().strip())
for i in range(1, n+1):
    stack = sys.stdin.readline().strip().split(" ")
    reversed = stack[::-1]
    print(f'Case #{i}:', ' '.join(reversed))