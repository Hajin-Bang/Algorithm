import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    A, B = map(int, input().split())
    
    while A != B:
        if A > B:
            A //= 2
        elif A < B:
            B //= 2
    print(10 * A)