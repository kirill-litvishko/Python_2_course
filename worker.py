import csv

id_counter = 1

class WorkerDB:

    def __init__(self):
        self.workers = []

    def add(self, worker):
        self.workers.append(worker)

    def read(self):
        for worker in self.workers:
            print(f"ID: {worker.getId()}, Name: {worker.name}, Surname: {worker.surname}, Department: {worker.dep}, Salary: {worker.salary}")

    def edit(self, worker_id, new_name, new_surname, new_dep, new_salary):
        for worker in self.workers:
            if worker.getId() == worker_id:
                worker.name = new_name
                worker.surname = new_surname
                worker.dep = new_dep
                worker.salary = new_salary

    def delete(self, worker_id):
        self.workers = [worker for worker in self.workers if worker.getId() != worker_id]


    @staticmethod
    def sort_dec(func):
        def wrapper(self, reverse=False):
            sorted_workers = sorted(self.workers, key=self.name)
            func(self, sorted_workers)
        return wrapper

    @sort_dec
    def sort(self, sorted_workers):
        for worker in sorted_workers:
            print(f"ID: {worker.getId()}, Name: {worker.name}, Surname: {worker.surname}, Department: {worker.dep}, Salary: {worker.salary}")

    @staticmethod
    def search_decorator(func):
        def wrapper(self, keyword):
            search_result = [worker for worker in self.workers if keyword.lower() in worker.name.lower() or keyword.lower() in worker.surname.lower()]
            func(self, search_result)
        return wrapper

    @search_decorator
    def search(self, search_result):
        for worker in search_result:
            print(f"ID: {worker.getId()}, Name: {worker.name}, Surname: {worker.surname}, Department: {worker.dep}, Salary: {worker.salary}")




class Worker:
    def __init__(self, name, surname, dep, salary):
        global id_counter
        self.__id = id_counter
        id_counter+=1
        self.name = name
        self.surname = surname
        self.dep = dep
        self.salary = salary

    def getId(self):
        return self.__id

    def setId(self, worker_id):
        self.__id = worker_id

with open("workers.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    worker_db = WorkerDB()
    for row in reader:
        worker = Worker(row['name'], row['surname'], row['dep'], row['salary'])
        worker_db.add(worker)

worker_db.read()
