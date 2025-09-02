# 导入抽象基类模块，用于定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod


# 定义员工抽象类（使用ABCMeta元类实现抽象类功能）
class Employee(metaclass=ABCMeta):
    """员工抽象类，定义所有员工的公共接口"""

    def __init__(self, name):
        self.name = name  # 员工姓名

    @abstractmethod
    def get_salary(self):
        """计算工资的抽象方法，所有子类必须实现此方法"""
        pass
    

# 经理类，继承自Employee抽象类
class Manager(Employee):
    """经理类，固定月薪制员工"""
    
    def get_salary(self):
        # 经理月薪固定为15000元
        return 15000.0  
    
# 程序员类，继承自Employee抽象类
class Programmer(Employee):
    """程序员类，按工作时长计算工资的员工"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)  # 调用父类构造方法初始化姓名
        self.working_hour = working_hour  # 工作时长（小时）

    def get_salary(self):
        # 程序员时薪200元，工资=时薪×工作时长
        return 200 * self.working_hour

# 销售员类，继承自Employee抽象类
class Salesman(Employee):
    """销售员类，按销售额提成计算工资的员工"""

    def __init__(self, name, sales=0):
        super().__init__(name)  # 调用父类构造方法初始化姓名
        self.sales = sales  # 销售额


    def get_salary(self):
        # 销售员底薪1800元 + 销售额5%提成
        return 1800 + self.sales * 0.05


# 创建员工列表，包含不同类型的员工
emps = [Manager('Make'), Programmer('Bob'), Manager('Alice'), Salesman('Tom')]

# 遍历员工列表，根据员工类型输入相应数据并计算工资
for emp in emps:
    if isinstance(emp, Programmer):
        # 为程序员输入本月工作时间
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        # 为销售员输入本月销售额
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    # 计算并打印工资
    print(f'{emp.name}本月工资为: {emp.get_salary()}元')
