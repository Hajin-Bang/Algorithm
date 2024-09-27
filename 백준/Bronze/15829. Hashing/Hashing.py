L = int(input())
input = input()
r = 31 

answer = 0

for i in range(len(input)):
    number = ord(input[i]) - 96
    answer += number * (r ** i)

print(answer % 1234567891)
