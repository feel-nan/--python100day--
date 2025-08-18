# 导入 random 模块，用于生成随机数
import random 
# 导入 time 模块，用于获取当前时间和实现程序暂停
import time

# 定义一个下载函数，用于模拟文件下载过程
# filename: 要下载的文件名
def download(filename):
  # 打印开始下载的提示信息
  print(f'开始下载{filename}.')
  # 程序暂停一段随机时间（0 到 6 秒之间），模拟下载耗时
  time.sleep(random.random() * 6)
  # 打印下载完成的提示信息
  print(f'{filename}下载完成.')


# 定义一个上传函数，用于模拟文件上传过程
# filename: 要上传的文件名
def upload(filename):
  # 打印开始上传的提示信息
  print(f'开始上传{filename}.')
  # 程序暂停一段随机时间（0 到 8 秒之间），模拟上传耗时
  time.sleep(random.random() * 8)
  # 打印上传完成的提示信息
  print(f'{filename}上传完成.') 


# 定义一个装饰器函数，用于记录函数的执行耗时
# func: 被装饰的函数
def record_time(func):
    # 定义一个包装函数，用于处理被装饰函数的调用
    def wrapper(*args, **kwargs):
        # 记录函数开始执行的时间
        start = time.time()
        # 调用被装饰的函数
        func(*args, **kwargs)
        # 记录函数结束执行的时间
        end = time.time()
        # 打印被装饰函数的执行耗时，保留两位小数
        print(f'{func.__name__}耗时：{end - start:.2f}秒')
    return wrapper

# 使用 record_time 装饰器修饰 download 函数，使其具备记录执行耗时的功能
# 等同于使用 @record_time 语法糖的效果
download = record_time(download)
# 使用 record_time 装饰器修饰 upload 函数，使其具备记录执行耗时的功能
# 等同于使用 @record_time 语法糖的效果
upload = record_time(upload)
# 调用 download 函数，下载名为 'Python从入门到放弃.pdf' 的文件
# 同时会自动记录该函数的执行耗时
download('Python从入门到放弃.pdf')
# 调用 upload 函数，上传名为 'MySQL从删库到跑路.avi' 的文件
# 同时会自动记录该函数的执行耗时
upload('MySQL从删库到跑路.avi ')
