class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f"{self.__name} is studying {course_name}.")

stu = Student('王大锤',20)
stu.study('Python')
# print(stu.__name)
print(stu._Student__name)
