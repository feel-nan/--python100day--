# 素数指的是只能被 1 和自身整除的大于 1 的整数。

# num = int(input('请输入一个数字：'))
# # 平方根取整，这是因为如果一个数不是素数，那么它一定存在一个小于或等于其平方根的因子。
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2,end + 1):
#   if num % i == 0:
#     is_prime = False
#     break
# if is_prime:
#   print(f'{num}是素数')
# else:
#   print(f'{num}不是素数')

# 素数指的是只能被 1 和自身整除的大于 1 的整数。
num = int(input('请输入一个数字：'))

# 处理小于等于 1 的情况
if num <= 1:
    print(f'{num}不是素数')
else:
    end = int(num ** 0.5)
    is_prime = True
    for i in range(2, end + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{num}是素数')
    else:
        print(f'{num}不是素数')
