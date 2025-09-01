# 定义一个名为 Person 的基类，表示人员的基本属性和行为
class Person:
    # 定义构造方法，初始化人员的姓名和年龄
    def __init__(self, name, age):
        self.name = name  # 存储人员的姓名
        self.age = age    # 存储人员的年龄

    # 定义吃饭方法，表示人员正在吃饭
    def eat(self):
        print(f'{self.name} is eating')

    # 定义睡觉方法，表示人员正在睡觉
    def sleep(self):
        print(f'{self.name} is sleeping')

    # 定义工作方法，表示人员正在工作
    def work(self):
        print(f'{self.name} is working')

# 定义一个名为 Student 的类，继承自 Person 类，表示学生
class Student(Person):
    
    # 定义构造方法，调用父类的构造方法初始化姓名和年龄
    def __init__(self, name, age):
        super().__init__(name, age)

    # 定义学习方法，接收课程名称作为参数，表示学生正在学习该课程
    def study(self, course_name):
        # 打印学生正在学习的课程信息
        print(f'{self.name} is studying {course_name}')


# 定义一个名为 Teacher 的类，继承自 Person 类，表示教师
class Teacher(Person):
    
    # 定义构造方法，调用父类的构造方法初始化姓名和年龄，并初始化教师职称
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title  # 存储教师的职称

    # 定义教学方法，接收课程名称作为参数，表示教师正在教授该课程
    def teach(self, course_name):
        print(f'{self.name} is teaching {course_name}')


# 创建一个名为 stu1 的 Student 对象，姓名为 Alice，年龄为 20
stu1 = Student('Alice', 20)
# 创建一个名为 stu2 的 Student 对象，姓名为 Bob，年龄为 22
stu2 = Student('Bob', 22)
# 创建一个名为 tea1 的 Teacher 对象，姓名为 Dr. Smith，年龄为 45，职称为 Professor
tea1 = Teacher('Dr. Smith', 45, 'Professor')

# 调用 stu1 的 eat 方法，表示 Alice 正在吃饭
stu1.eat()
# 调用 stu2 的 sleep 方法，表示 Bob 正在睡觉
stu2.sleep()
# 调用 tea1 的 eat 方法，表示 Dr. Smith 正在吃饭
tea1.eat()
# 调用 stu1 的 study 方法，表示 Alice 正在学习 Math
stu1.study('Math')
# 调用 tea1 的 teach 方法，表示 Dr. Smith 正在教授 English
tea1.teach('English')
# 调用 stu2 的 study 方法，表示 Bob 正在学习 Science
stu2.study('Science')
# 注释：打印 stu1 的姓名和年龄（当前处于注释状态，未执行）
# print(stu1.name, stu1.age)
