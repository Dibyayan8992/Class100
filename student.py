class Student(object):
    def __init__(self, name, age, gender, level, grades = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades
    def setGrade(self, course, grade):
        self.grades[course] = grade
    def setGrade(self, course):
        return self.grades[course]
    def getCGPA(self):
        return sum(self.grades.values())/len(self.grades)

dibya = Student("Dibyayan", 15, "Male", 9, {"Computer":9.5})
print(dibya.age)