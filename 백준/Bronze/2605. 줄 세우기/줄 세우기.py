studentNumber = int(input())
numbers = list(map(int, input().split()))
students = []
for i in range(studentNumber):  
    students.insert(i-numbers[i], i+1)

result = ' '.join(map(str, students))
print(result)