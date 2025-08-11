# # 定义一个名为 calc 的函数，使用可变位置参数 *args 和可变关键字参数 **kwargs
# # 该函数用于将传入的整数和浮点数参数相加并返回结果
# def calc(*args, **kwargs):
#     # 将位置参数和关键字参数的值合并为一个列表
#     items = list(args) + list(kwargs.values())
#     # print(items)

#     # 初始化结果变量为 0
#     result = 0
#     # 遍历合并后的参数列表
#     for item in items:
#         # 检查当前参数的类型是否为整数或浮点数
#         if type(item) in (int, float):
#             # 如果是整数或浮点数，则累加到结果变量中
#             result += item
#     # 返回累加结果
#     return result


# # 调用 calc 函数，传入位置参数 1, 2, 3 和关键字参数 a=4, b=5，并打印结果
# print(calc(1, 2, 3, a=4, b=5))






