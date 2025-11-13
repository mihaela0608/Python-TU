class Person:
    def __init__(self, fname, lname, age, nationality):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.nationality = nationality
    def print(self):
        print(f"Name: {self.firstname} {self.lastname} - {self.nationality}")

class Student(Person):
    def __init__(self, fname, lname, age, nationality, university, year):
        super().__init__(fname, lname, age, nationality)
        self.university = university
        self.year = year
    
    def print(self):
        print(f"Name: {self.firstname} {self.lastname} - {self.nationality} in {self.university} year: {year}")


for i in range(2):
    name = input("First name: ")
    lname= input("Last name: ")
    age = input("Age: ")
    nationality = input("Nationality: ")
    uni = input("University: ")
    year = input("Year: ")

    MyStudent = Student(name, lname, age, nationality, uni, year)
    
    MyStudent.print()

