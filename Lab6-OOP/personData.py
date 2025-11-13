class Person:
    def __init__(self, fname, lname, age, nationality):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.nationality = nationality
    def print(self):
        print(f"Name: {self.firstname} {self.lastname} - {self.nationality}")

for i in range(2):
    name = input("First name: ")
    lname= input("Last name: ")
    age = input("Age: ")
    nationality = input("Nationality: ")

    MyPerson = Person(name, lname, age, nationality)
    
    MyPerson.print()

