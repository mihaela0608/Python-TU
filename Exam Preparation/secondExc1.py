class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age
    def worker_information(self):
        print(f"{self.fname} {self.lname} with number: {self.worker_num} has {self.work_experience_company} years of experiecne with salary- {self.salary} at {self.age}")
    def salary_bonus(self):
        bonus = 0
        if self.work_experience_company>= 5 and self.work_experience_company <= 10:
            bonus = self.salary + self.salary*0.015
        elif self.work_experience_company > 10:
            bonus = self.salary + self.salary*0.02
        else:
            bonus = self.salary + self.salary*0.005
workers_list = []
n = int(input("Workers count: "))
for i in range(n):
    num = input()
    fname = input()
    lname = input()
    work_exp = input()
    salary = input()
    age = input()
    worker = Worker(num, fname, lname, work_exp, salary, age)
    workers_list.append(worker)

def search_by_num(workers_list, workers_num):
    for w in workers_list:
        if(w.worker_num == workers_num):
            return True
    return False

def search_by_name_experience(workers_list, fname, work_experience_company):
    newList = []
    for w in workers_list:
        if(w.fname == fname and w.work_experience_company == work_experience_company):
            newList.append(w)
    return newList
def add_worker(workers_list, worker):
    workers_list.append(worker)
def remove_worker(workers_list, worker_num):
    removed = False
    for w in workers_list:
        if(worker_num == w.worker_num):
            removed = True
            workers_list.remove(w)
            break
    if(removed):
        print("Information deleted !!!")
    else:
        print("Wrong worker num!!!")
    
