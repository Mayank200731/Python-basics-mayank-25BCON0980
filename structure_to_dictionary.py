class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

s = Student("Mayank", 20, "CSE")

student_dict = vars(s)  # or s.__dict__

print(student_dict)
