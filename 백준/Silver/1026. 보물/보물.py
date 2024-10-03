import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
S = 0

for i in range(N):
    b_max = max(B)
    S += A[i] * b_max # A의 최솟값과 B의 최댓값을 곱한다. 
    B.remove(b_max) # b_max에 해당하는 값을 찾아서 제거한다. 

print(S)