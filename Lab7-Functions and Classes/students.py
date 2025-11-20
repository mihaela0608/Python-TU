studentsList = []
for i in range(2):
    name = input(f"Name {i+1}: ")
    age = int(input(f"Age {i+1}: "))
    grade = float(input(f"Grade {i+1}: "))
    town = input(f"Town {i+1}: ")

    student = (name, age, grade, town)
    studentsList.append(student)

students = tuple(studentsList)

def good_students(students):
    total = sum(map(lambda x: x[2], students))
    print(f"The students are doing great with average grade {total / 2}")

good_students(students)
    

    