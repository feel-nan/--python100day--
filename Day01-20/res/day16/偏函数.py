# partial 函数来自 Python 的 functools 模块，用于创建偏函数。
# “partial 函数的第一个参数和返回值都是函数” 这句话可以从以下两个方面理解：

# 第一个参数是函数
# partial 函数的第一个参数需要传入一个原函数，也就是你想要对其部分参数进行固定的函数。
# 后续参数则是要固定给原函数的参数值。下面是调用格式和示例代码：



from functools import partial

# 定义一个原函数，用于计算两个数的乘积
def multiply(x, y):
    return x * y

# 使用 partial 函数创建一个新的偏函数，固定第一个参数为 2
# 这里 multiply 作为 partial 的第一个参数传入
double = partial(multiply, 2)

print(double(4))  # 输出: 8
# 在上述代码中，multiply 函数作为 partial 的第一个参数传入，
# 后续固定了 multiply 的第一个参数 x 的值为 2，从而得到一个新的偏函数 double。

# 返回值是函数
# partial 函数执行后会返回一个新的函数（即偏函数）。
# 这个新函数相当于原函数的一个“简化版”，它固定了原函数的部分参数，调用时只需传入剩余的参数即可14。

# 在上面的例子中，partial(multiply, 2) 返回的 double 就是一个新的函数。
# 调用 double(4) 时，实际上相当于调用 multiply(2, 4)。