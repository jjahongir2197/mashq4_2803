class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    def info(self):
        return f"{self.name} | {self.salary}"


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        self.employees.append(Employee(name, salary))

    def show_employees(self):
        for i, e in enumerate(self.employees):
            print(i+1, e.info())

    def increase_salary(self, index, percent):
        if 0 <= index < len(self.employees):
            self.employees[index].increase_salary(percent)


def run():
    company = Company()

    while True:
        print("\n1 Add Employee")
        print("2 Show Employees")
        print("3 Increase Salary")
        print("4 Exit")

        c = input()

        if c == "1":
            name = input("Name: ")
            salary = int(input("Salary: "))
            company.add_employee(name, salary)

        elif c == "2":
            company.show_employees()

        elif c == "3":
            company.show_employees()
            i = int(input("Employee: ")) - 1
            p = int(input("Percent: "))
            company.increase_salary(i, p)

        else:
            break


run()
