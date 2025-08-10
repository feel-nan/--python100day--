# 导入 random 模块，用于生成随机数
import random

# 生成 1 到 33 的红球列表，双色球的红球范围是 1 - 33
RED_BALLS = [i for i in range(1, 34)]  
# 生成 1 到 16 的蓝球列表，双色球的蓝球范围是 1 - 16
BLUE_BALLS = [i for i in range(1, 17)]  

# 定义一个函数，用于随机选择一组双色球号码
def choose():
    # 从红球列表中随机无放回地选择 6 个红球
    selected_balls = random.sample(RED_BALLS, 6) 
    # 对选择的红球进行升序排序
    selected_balls.sort()  # 红球排序
    # 从蓝球列表中随机选择 1 个蓝球，并添加到已选号码列表末尾
    selected_balls.append(random.choice(BLUE_BALLS)) 
    # 返回这组包含 6 个红球和 1 个蓝球的号码
    return selected_balls


# 定义一个函数，用于显示一组双色球号码，红球显示为红色，蓝球显示为蓝色
def display(balls):
    # 遍历前 6 个红球并打印，使用红色 ANSI 转义码显示
    for ball in balls[:-1]:
        print(f'\033[31m{ball:02d}\033[0m', end=' ')
    # 打印最后一个蓝球，使用蓝色 ANSI 转义码显示
    print(f'\033[34m{balls[-1]:02d}\033[0m') 

# 获取用户输入，确定需要生成的双色球号码数量
num = int(input("请输入需要生成的双色球号码数量: "))
# 循环生成并显示指定数量的双色球号码
for _ in range(num):
    # 调用 choose 函数生成一组号码，并调用 display 函数显示
    display(choose())
