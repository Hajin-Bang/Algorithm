import sys

input = sys.stdin.readline
N = int(input())
requests = list(map(int, input().split()))
limit = int(input())

def binary_search(arr, start, end, limit):
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for request in arr:
            if request <= mid:
                total += request
            elif request > mid:
                total += mid 
    
        if total > limit:
            end = mid - 1
        else:
            start = mid + 1

    return end

print(binary_search(requests, 0, max(requests), limit))