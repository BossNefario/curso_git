if __name__ == '__main__':
    students_grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grade.append((name ,score))
    sorted_grades = sorted(list(set(x[1] for x in students_grade)))
    second_lowest = sorted_grades[1]

    sec_lowest_final = []
    for student in students_grade:
        if second_lowest == student[1]:
            sec_lowest_final.append(student[0])
    
    for student in sorted(sec_lowest_final):
        print(student)
