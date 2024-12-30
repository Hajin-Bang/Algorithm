input = input()
list = input.split('-')

result = sum(map(int, list[0].split('+')))
for i in list[1:]:
    cal = sum(map(int, i.split('+'))) 
    result -= cal 

print(result)