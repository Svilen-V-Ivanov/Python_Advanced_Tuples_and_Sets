students = int(input())

def aver(values):
    return sum(values) / len(values)

students_grades = {}

for _ in range(students):
    student, grade_string = input().split(' ')
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(float(grade_string))

for student, grades in students_grades.items():
    grades_formated = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_avg = aver(grades)
    grades_avg_formatted = f'{grades_avg:.2f}'
    print(f'{student} -> {grades_formated} (avg: {grades_avg_formatted})')

