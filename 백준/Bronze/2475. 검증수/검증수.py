nums = input().split()
sum = 0 
for num in nums:
    sum += int(num) ** 2
    
print(sum % 10)