if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
    list = sorted(list, key=lambda x: x[1])  
    lowest = list[0][1]
    
    second_lowest = None
    for student in list:
        if(student[1] > lowest):
            second_lowest = student[1]
            break
    
    students = [student[0] for student in list if student[1] == second_lowest]
    # print(students)
    
    students.sort()
    for student in students:
        print(student)