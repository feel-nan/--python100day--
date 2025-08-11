# 定义一个名为 calc 的函数，用于对传入的数值执行指定的二元操作
# init_value: 初始值，操作的起始值
# op_func: 二元操作函数，用于对两个数值进行操作
# *args: 可变位置参数，存储额外的位置参数数值
# **kwargs: 可变关键字参数，存储额外的关键字参数数值
def calc(init_value, op_func, *args, **kwargs):
    # 将位置参数和关键字参数的值合并为一个列表
    items = list(args) + list(kwargs.values())
    # 初始化结果变量为初始值
    result = init_value
    # 遍历合并后的参数列表
    for item in items:
        # 检查当前参数的类型是否为整数或浮点数
        if type(item) in (int, float):
            # 使用传入的二元操作函数对结果和当前参数进行操作
            result = op_func(result, item)
    # 返回最终的操作结果
    return result

# 定义一个名为 add 的函数，用于实现两个数的加法操作
# x: 第一个加数
# y: 第二个加数
# 返回: 两个数相加的结果
# def add(x, y):
#     return x + y

# 定义一个名为 mul 的函数，用于实现两个数的乘法操作
# x: 第一个乘数
# y: 第二个乘数
# 返回: 两个数相乘的结果
# def mul(x, y):
#     return x * y

# 调用 calc 函数，使用加法操作对数值进行累加，并打印结果
# print(calc(0, add, 1, 2, 3, a=4, b=5))
# 调用 calc 函数，使用乘法操作对数值进行累乘，并打印结果
# print(calc(1, mul, 1, 2, 3, a=4, b=5))



# 定义一个名为 is_even 的函数，用于判断一个数是否为偶数
# num: 需要判断的整数
# 返回: 如果 num 是偶数返回 True，否则返回 False
def is_even(num):
    return num % 2 == 0

# 定义一个名为 square 的函数，用于计算一个数的平方
# num: 需要计算平方的数
# 返回: num 的平方值
def square(num):
    return num ** 2

# 定义一个包含多个整数的列表
old_nums = [12,45,78,35,79,0]
# 使用 filter 函数过滤出 old_nums 中的偶数，再使用 map 函数对这些偶数求平方
# 最后将结果转换为列表
# filter(is_even, old_nums): 过滤出 old_nums 中满足 is_even 函数条件（偶数）的元素
# map(square, ...): 对过滤后的偶数元素应用 square 函数，计算其平方
# list(...): 将 map 对象转换为列表
new_nums = list(map(square, filter(is_even, old_nums)))
# 打印经过过滤和平方操作后的新列表
print(new_nums)

