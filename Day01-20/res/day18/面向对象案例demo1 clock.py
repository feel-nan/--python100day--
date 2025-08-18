# > **要求**：定义一个类描述数字时钟，提供走字和显示时间的功能。
# 导入 time 模块，用于使用 sleep 函数实现计时功能
import time

# 定义一个名为 Clock 的类，用于模拟时钟功能
class Clock:
    
    # 定义构造方法，初始化时钟的时、分、秒。参数均有默认值 0
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour  # 存储时钟的小时数
        self.min = minute  # 存储时钟的分钟数
        self.sec = second  # 存储时钟的秒数

    # 定义运行方法，用于使时钟的秒数递增，并处理进位逻辑
    def run(self):
        self.sec += 1  # 秒数加 1
        if self.sec == 60:  # 当秒数达到 60 时
            self.sec = 0  # 秒数归零
            self.min += 1  # 分钟数加 1
            if self.min == 60:  # 当分钟数达到 60 时
                self.min = 0  # 分钟数归零
                self.hour += 1  # 小时数加 1
                if self.hour == 24:  # 当小时数达到 24 时
                    self.hour = 0  # 小时数归零

    # 定义显示方法，用于返回格式化后的时间字符串
    def show(self):
        # 使用格式化字符串，确保时、分、秒均为两位数，不足补 0
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

# 创建一个 Clock 类的实例，初始时间设置为 23 时 59 分 58 秒
clock = Clock(23, 59, 58)
# 进入无限循环，模拟时钟持续运行
while True:
    print(clock.show())  # 打印当前时钟显示的时间
    time.sleep(1)  # 程序暂停 1 秒，模拟每秒更新一次时间
    clock.run()  # 调用 run 方法，更新时钟的时间
