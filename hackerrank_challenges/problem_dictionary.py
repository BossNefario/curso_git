if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    check = student_marks[query_name]
    media = sum(check) / len(check)
    print(f'{media:.2f}%') 

