import sys
test_case = int(sys.stdin.readline().strip())


for i in range(test_case):
    items = {}

    n = int(sys.stdin.readline().strip())
    for i in range(n):
        item_name, category = sys.stdin.readline().strip().split()

        # 해당 category의 의상이 이미 있을 때
        if category in items:
            items[category].append(item_name) # 의상을 리스트에 담음 => [의상1, 의상2~] 
        else: 
            items[category] = [item_name] # items에 추가
    
    # 경우의 수 계산
    combinations = 1
    for category in items:
        combinations *= len(items[category]) + 1

    print(combinations - 1) # 아무것도 고르지 않은 경우 하나를 뺀다. 