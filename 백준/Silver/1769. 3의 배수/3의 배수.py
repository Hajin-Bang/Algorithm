from functools import reduce

n = input()
stack = list(map(int, n))
count = 0

while len(stack)>1:
    sum = reduce(lambda x,y: x+y, stack)
    stack = list(map(int, str(sum)))
    count += 1

result = "YES" if stack[0] % 3 == 0 else "NO"
print(count)
print(result)
