import sys

input = sys.stdin.readline

subjects = {}

grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

for _ in range(20):
    subject, credit, grade = input().split()
    if grade != 'P':  
        subjects[subject] = [float(credit), grade]

total = 0
total_credit = 0
for key in subjects:
    credit = subjects[key][0]
    grade = subjects[key][1]
    grade_number = grades[grade]

    total += credit * grade_number
    total_credit += credit

result = total/total_credit
print(f"{result:.6f}")
