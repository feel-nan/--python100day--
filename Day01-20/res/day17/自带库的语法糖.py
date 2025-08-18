# 导入 random 模块，用于生成随机数
import random
# 导入 time 模块，用于获取当前时间和实现程序暂停
import time

# 从 functools 模块导入 wraps 装饰器，用于保留被装饰函数的元信息
from functools import wraps

# 定义一个装饰器函数，用于记录函数的执行耗时
# func: 被装饰的函数
def record_time(func):
    # 使用 wraps 装饰器保留被装饰函数的元信息，如 __name__、__doc__ 等
    @wraps(func)
    # 定义一个包装函数，用于处理被装饰函数的调用
    def wrapper(*args, **kwargs):
        # 记录函数开始执行的时间
        start = time.time()
        # 调用被装饰的函数并保存返回结果
        result = func(*args, **kwargs)
        # 记录函数结束执行的时间
        end = time.time()
        # 打印被装饰函数的执行耗时，保留两位小数
        print(f'{func.__name__}耗时：{end - start:.2f}秒')
        # 返回被装饰函数的执行结果
        return result
    return wrapper

# 使用 record_time 装饰器修饰 download 函数，使其具备记录执行耗时的功能
# filename: 要下载的文件名
@record_time
def download(filename):
    # 打印开始下载的提示信息
    print(f'开始下载{filename}.')
    # 程序暂停一段随机时间（0 到 6 秒之间），模拟下载耗时
    time.sleep(random.random() * 6)
    # 打印下载完成的提示信息
    print(f'{filename}下载完成.')

# 使用 record_time 装饰器修饰 upload 函数，使其具备记录执行耗时的功能
# filename: 要上传的文件名
@record_time
def upload(filename):
    # 打印开始上传的提示信息
    print(f'开始上传{filename}.')
    # 程序暂停一段随机时间（0 到 8 秒之间），模拟上传耗时
    time.sleep(random.random() * 8)
    # 打印上传完成的提示信息
    print(f'{filename}上传完成.')

# 调用被 record_time 装饰后的 download 函数，下载指定文件并记录耗时
# 传入文件名 'Python从入门到放弃.pdf'
download('Python从入门到放弃.pdf')
# 调用被 record_time 装饰后的 upload 函数，上传指定文件并记录耗时
# 传入文件名 'MySQL从删库到跑路.avi '
upload('MySQL从删库到跑路.avi ')
# 调用 download 函数的原始版本，跳过 record_time 装饰器的耗时记录功能
# 传入文件名 'Python从入门到放弃.pdf'
download.__wrapped__('Python从入门到放弃.pdf')
# 调用 upload 函数的原始版本，跳过 record_time 装饰器的耗时记录功能
# 传入文件名 'MySQL从删库到跑路.avi '
upload.__wrapped__('MySQL从删库到跑路.avi ')
