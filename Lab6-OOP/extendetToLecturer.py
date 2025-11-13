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
        super().print()
        print(f"{self.university} year: {self.year}")

class Lecturer(Person):
    def __init__(self, fname, lname, age, nationality, university, experience):
        super().__init__(fname, lname, age, nationality)
        self.university = university
        self.experience = experience
    def print(self):
        super().print()
        print(f"{self.university} experience: {self.experience}")

for i in range(2):
    name = input("First name: ")
    lname= input("Last name: ")
    age = input("Age: ")
    nationality = input("Nationality: ")
    uni = input("University: ")
    exp = input("Experience: ")

    MyLecturer = Lecturer(name, lname, age, nationality, uni, exp)
    
    MyLecturer.print()

