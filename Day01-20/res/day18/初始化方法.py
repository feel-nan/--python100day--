# 定义一个名为 Student 的类，用于表示学生对象
class Student:
    # 定义构造方法，初始化学生的姓名和年龄
    def __init__(self, name, age):
        self.name = name  # 存储学生的姓名
        self.age = age    # 存储学生的年龄

    # 定义学习方法，接收课程名称作为参数
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    # 定义玩耍方法，用于表示学生正在玩游戏
    def play(self):
        print(f'{self.name}正在玩游戏.')

# 创建一个名为 stu1 的 Student 对象，姓名为张三，年龄为 18
stu1 = Student('张三', 18)
# 创建一个名为 stu2 的 Student 对象，姓名为李四，年龄为 19
stu2 = Student('李四', 19)
# 调用 stu1 的 study 方法，学习 Python 程序设计
stu1.study('Python程序设计')
# 调用 stu2 的 play 方法，表示李四正在玩游戏
stu2.play()
