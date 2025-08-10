# 定义一个函数 num，用于计算两个整数的最小公倍数
# 参数 x 和 y 为需要计算最小公倍数的两个整数，返回值为它们的最小公倍数
def num(x:int,y:int) -> int:
    # 通过公式 x * y / gcd(x, y) 计算最小公倍数
    return x*y//gcd(x,y)

# 定义一个函数 gcd，用于计算两个整数的最大公约数
# 参数 x 和 y 为需要计算最大公约数的两个整数，返回值为它们的最大公约数
def gcd(x:int,y:int) -> int:
    # 使用辗转相除法计算最大公约数
    while y % x != 0:
        x,y = y % x,x
    return x

# # 打印 50 和 16 的最小公倍数
# print(num(50,16))
# # 打印 50 和 16 的最大公约数
# print(gcd(50,16))
