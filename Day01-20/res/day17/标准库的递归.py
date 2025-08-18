# 从 functools 模块导入 lru_cache 装饰器，用于实现函数结果的缓存
from functools import lru_cache

# 使用 lru_cache 装饰器，对 fib1 函数的结果进行缓存，提高递归计算的效率
# 避免重复计算相同参数的函数调用
@lru_cache()
# 定义一个递归函数，用于计算斐波那契数列的第 n 项
# n: 斐波那契数列的项数
def fib1(n):
  # 当 n 为 1 或 2 时，斐波那契数列的值为 1，这是递归的终止条件
  if n in (1, 2):
    return 1
  # 递归调用 fib1 函数，计算第 n 项的值
  return fib1(n - 1) + fib1(n - 2)


# 使用 for 循环遍历 1 到 50 的整数
for i in range(1, 51):
  # 调用 fib1 函数计算斐波那契数列的第 i 项，并打印结果
  print(fib1(i))
