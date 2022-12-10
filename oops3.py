#dunder methods
class Employee:
    def __init__(self,name,age,role,salary):
        self.name=name
        self.age=age
        self.role=role
        self.salary=salary
    def print_details(self):
        print(f"Employe's name is {self.name} \n {self.name}'s age is {self.age}\n {self.name}'s role is {self.role} and \nsalary is {self.salary} ")
sabin= Employee("Sabin Bhomjan",18,"Video Editor ",70000)
sabin.print_details()