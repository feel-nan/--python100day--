# 导入 random 模块，用于生成随机数
import random
# 导入 string 模块，用于获取预定义的字符集
import string

# 定义 ALL_CHARS 变量，将数字字符集和大小写字母字符集拼接起来
ALL_CHARS = string.digits + string.ascii_letters

# 定义生成随机验证码的函数，code_len 为验证码长度，默认值为 4
# 使用仅限关键字参数（*）确保调用时必须通过参数名指定 code_len
def generate_random_code(*, code_len = 4):
    # 使用 random.choices 从 ALL_CHARS 中随机选择 code_len 个字符
    # 然后使用 ''.join 将这些字符拼接成字符串
    return ''.join(random.choices(ALL_CHARS, k=code_len))

# 循环 5 次，每次调用 generate_random_code 函数生成一个随机验证码并打印
# for _ in range(5):
#     print(generate_random_code())
