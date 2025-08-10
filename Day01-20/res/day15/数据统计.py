# 计算数据集的极差（最大值与最小值的差值）
# 参数 data: 输入的数据集，应为可迭代对象
# 返回值: 数据集的极差
def ptp(data):
    return max(data) - min(data)

# 计算数据集的均值（平均值）
# 参数 data: 输入的数据集，应为可迭代对象
# 返回值: 数据集的均值
def mean(data):
    return sum(data) / len(data)

# 计算数据集的中位数
# 参数 data: 输入的数据集，应为可迭代对象
# 返回值: 数据集的中位数
def median(data):
    # 对数据集进行排序，并获取数据集的长度
    temp, size = sorted(data), len(data)
    # 如果数据集长度为奇数，直接返回中间元素
    if size % 2 != 0:
        return temp[size // 2]
    # 如果数据集长度为偶数，返回中间两个元素的均值
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])

# 计算数据集的方差
# 参数 data: 输入的数据集，应为可迭代对象
# 参数 ddof: 自由度，默认值为 1
# 返回值: 数据集的方差
def var(data, ddof=1):
    # 计算数据集的均值
    x_bar = mean(data)
    # 计算每个数据点与均值的差的平方
    temp = [(num - x_bar)**2 for num in data]
    # 计算方差，自由度为 ddof
    return sum(temp) / (len(data) - ddof)

# 计算数据集的标准差
# 参数 data: 输入的数据集，应为可迭代对象
# 参数 ddof: 自由度，默认值为 1
# 返回值: 数据集的标准差
def std(data, ddof=1):
    # 标准差为方差的平方根
    return var(data, ddof)**0.5

# 计算数据集的变异系数
# 参数 data: 输入的数据集，应为可迭代对象
# 参数 ddof: 自由度，默认值为 1
# 返回值: 数据集的变异系数
def cv(data, ddof=1):
    # 变异系数为标准差与均值的比值
    return std(data, ddof) / mean(data)

# 打印数据集的各项统计信息
# 参数 data: 输入的数据集，应为可迭代对象
def describe(data):
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')


# print("数据集的各项统计信息:")
# print("数据集: [10, 12, 23, 23, 16, 23, 21, 16]")
# describe([10, 12, 23, 23, 16, 23, 21, 16])
