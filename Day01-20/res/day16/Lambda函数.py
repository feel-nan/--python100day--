# 定义一个旧列表，包含一些整数示例
# old_nums = [35, 12, 8, 99, 60, 52]
# 使用 map 和 filter 结合 lambda 函数，先筛选出旧列表中的偶数，再对这些偶数求平方，最后转换为列表
# new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
# 打印处理后的新列表
# print(new_nums)


# 导入 functools 模块，该模块提供了一些高阶函数
import functools
# 导入 operator 模块，该模块提供了一系列操作符对应的函数
import operator

# 使用 lambda 函数和 functools.reduce 实现阶乘计算
# functools.reduce(operator.mul, range(1, n + 1), 1) 会将 1 到 n 的所有数字相乘
fac = lambda n: functools.reduce(operator.mul, range(1, n + 1), 1)

# 使用 lambda 函数和 all、map 实现素数判断
# all(map(lambda f: x % f, range(2,int(x ** 0.5) + 1))) 会检查 x 是否能被 2 到 sqrt(x) 之间的任何数整除
is_prime = lambda x: all(map(lambda f: x % f, range(2,int(x ** 0.5) + 1)))

# 打印 5 的阶乘
print(fac(5))
# 打印 7 是否为素数的判断结果
print(is_prime(7))
