# 定义一个名为 Student 的类，用于表示学生对象
class Student:
  # 定义一个实例方法 study，用于表示学生学习某门课程的行为
  # self: 代表类的实例对象本身
  # course_name: 要学习的课程名称
  def study(self, course_name):
    # 打印学生正在学习某门课程的信息
    print(f'学生正在学习{course_name}.')
  
  # 定义一个实例方法 play，用于表示学生玩耍的行为
  # self: 代表类的实例对象本身
  def play(self):
    # 打印学生正在玩耍的信息
    print(f'学生正在玩耍.')
