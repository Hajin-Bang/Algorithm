import sys

input = sys.stdin.readline

N = int(input())
first_word = input().strip()
second_word = input().strip()

first = [] 
second = []
for i in first_word:
    first.append(i)
for j in second_word:
    second.append(j)

remove_word = ['a','e','i','o','u']

# 조건 2
if first[0] != second[0] or first[-1] != second[-1]:
    print("NO")
else: 
    first_remove = ""
    for word in first_word:
        if word not in remove_word:
            first_remove += word

    second_remove = ""
    for word in second_word:
        if word not in remove_word:
            second_remove += word

    # 조건 3
    if first_remove != second_remove:
        print("NO")
    
    else: 
        # 조건 1
        if sorted(first_word) != sorted(second_word):
            print("NO")
        else:
            print("YES")