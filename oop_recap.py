class Student:
    __slots__ = ['id', 'name', 'grade']
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

s = Student(1, "Moaz", -10)
s2 = Student(2, "Moaz", -100)
print(Student.__dict__)
print("=============")
# never do this
Student.__slots__.append("city")
print(Student.__dict__)

s2.city = "Alex"

