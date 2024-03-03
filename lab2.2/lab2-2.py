def calculateGrades(filePath):

    with open(filePath, 'r') as file:
        students = file.readlines()

        totalGrade = 0
        numOfStudents = 0

        for student in students:
            studentData = student.split(' ')
            name = studentData[0]
            grade = float(studentData[1])
            print(f"The student's {name} grade is: {grade}")
            if grade < 60:
                print(f"{name} has failed.")
            totalGrade += grade
            numOfStudents += 1

        averageGrade = totalGrade / numOfStudents
        print(f"\naverage grade of all students: {averageGrade:.2f}")


calculateGrades("./students.txt") 