n = int(input())
start, end = 1, 1
sum = 1
count = 1

while end != n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(count)