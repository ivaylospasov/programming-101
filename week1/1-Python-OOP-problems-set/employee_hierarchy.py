#!/usr/bin/env python3


class Employee:

    def __init__(self, sirname, name, work_hours):
        self.sirname = sirname
        self.name = name
        self.work_hours = work_hours


class HourlyEmployee(Employee):

    def __init__(self, sirname, name, work_hours):
        super().__init__(sirname, name, work_hours)


class SalariedEmployee(Employee):

    def __init__(self, sirname, name, work_hours):
        super().__init__(sirname, name, work_hours)


class Manager(Employee):
    def __init__(self, sirname, name, work_hours):
        super().__init__(sirname, name, work_hours)


def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff:
        hours = int(input("Hours worked by " + employee.getName() + ": "))
        pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)

if __name__ == '__main__':
    main()
