# 定义一个名为 is_prime 的函数，用于判断一个数是否为素数
# 函数接收一个整数类型的参数 num，并返回一个布尔值
def is_prime(num:int) -> bool:
    # 从 2 开始遍历到 num 的平方根（取整后加 1）
    # 因为如果一个数不是素数，那么它一定有一个小于或等于其平方根的因子
    for i in range(2, int(num**0.5) + 1): 
        # 如果 num 能被 i 整除，说明 num 不是素数
        if num % i == 0:
            return False
    # 如果遍历完所有可能的因子都没有找到能整除 num 的数，说明 num 是素数
    return True

# # 提示用户输入一个整数，并将输入转换为整数类型
# NUM = int(input("请输入一个整数: "))
# # 调用 is_prime 函数判断 NUM 是否为素数，并打印结果
# print(is_prime(NUM))
