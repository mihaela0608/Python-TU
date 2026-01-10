class Employee:
    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = int(work_experience)
        self.educarion_level = education_level
        self.salary = float(salary)
        self.age = int(age)
    def display_info(self):
        print(f"{self.fname} {self.lname}- {self.i_num}, has {self.work_experience} years of experience and {self.educarion_level} education level, salary: {self.salary} leva {self.age} years old ")
    def bonus(self):
        bonus = 0
        if(self.educarion_level == "Висше"):
            bonus = self.salary * 0.05
        elif(self.educarion_level == "Средно"):
            bonus = self.salary * 0.02
        bonus+= self.work_experience*(self.salary*0.012)
employee_list = []
count = int(input("Count employees: "))
for i in range(count):
    fn = input("First name")
    ln = input("Last name")
    w_e = int(input("Experience: "))
    e_l = input("Education level: ")
    salary = float(input("Salary "))
    age = int(input("Age: "))

def sort_employee(employee_list):
    sorted_list = sorted(employee_list, key= lambda a: a.age)
    for e in sorted_list:
        e.display_info()
def search_by_name(emplyee_list, name, lname):
    for e in employee_list:
        if e.fname == name and e.lname == lname:
            e.display_info()
            return
    print("Not found!!!")
def remove_employee(employee_list, i_num):
    for e in employee_list:
        if e.i_num == i_num:
            employee_list.remove(e)
            print("Information deleted!!!")
            return
    print("Wrong i_num")
    