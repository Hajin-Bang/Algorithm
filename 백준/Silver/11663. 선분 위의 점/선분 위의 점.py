import sys

input = sys.stdin.readline

def lower(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left+right) // 2
        if arr[mid] < target:
            left = mid + 1
        else: 
            right = mid
    return left

def upper(arr, target):
    left, right = 0, len(arr)
    while left<right:
        mid = (left + right) // 2
        if arr[mid] <=target:
            left = mid + 1
        else:
            right = mid
    return left

n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]
result = []

points.sort() 

for start, end in segments:
    left_idx = lower(points, start)
    right_idx = upper(points, end)
    result.append(right_idx - left_idx)

for i in result:
    print(i)