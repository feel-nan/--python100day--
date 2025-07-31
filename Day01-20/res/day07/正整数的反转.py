# 从用户输入中获取一个整数，并将其赋值给变量 num
num = int(input('num = '))
# 初始化一个变量 reversed_num，用于存储反转后的整数，初始值为 0
reversed_num = 0
# 当 num 大于 0 时，执行循环体中的代码
while num > 0:
  # 将 reversed_num 乘以 10，再加上 num 的个位数，更新 reversed_num 的值
  reversed_num = reversed_num * 10 + num % 10
  # 使用整除运算符 // 将 num 除以 10，去掉 num 的个位数，更新 num 的值
  num //= 10
# 输出反转后的整数
print(reversed_num)
