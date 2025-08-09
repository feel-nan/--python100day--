# if __name__ == "__main__":
#   def fac(n):
#     result = 1
#     for i in range(2,n+1):
#       result *= i
#     return result

# a = int(input("请输入一个整数："))
# b = int(input("请输入另一个整数："))
# print(fac(a) // fac(b) // fac(a-b))
# 计算阶乘


# from math import factorial

# m = int(input('m = '))
# n = int(input('n = '))
# print(factorial(m) // factorial(n) // factorial(m - n))

# 这段代码里factorial名字太长，不方便
from math import factorial as f
m = int(input('m = '))
n = int(input('n = '))
print(f(m) // f(n) // f(m - n))