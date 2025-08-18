# >  **要求**：定义一个类描述平面上的点，提供计算到另一个点距离的方法。
# 定义一个名为 Point 的类，用于表示平面上的点
class Point:
    # 定义构造方法，初始化点的坐标。参数 x 和 y 均有默认值 0
    def __init__(self, x=0, y=0):
        self.x = x  # 存储点的 x 坐标
        self.y = y  # 存储点的 y 坐标

    # 定义计算两点之间距离的方法，接收另一个 Point 类的实例作为参数
    def distance_to(self, other):
        dx = self.x - other.x  # 计算两点在 x 轴上的距离差
        dy = self.y - other.y  # 计算两点在 y 轴上的距离差
        # 使用勾股定理计算两点之间的距离并返回
        return (dx**2 + dy**2) ** 0.5

    # 定义魔术方法，将点对象转换为字符串表示形式
    def __str__(self):
        # 返回格式化后的坐标字符串，格式为 (x,y)
        return f'({self.x},{self.y})'

# 创建一个 Point 类的实例 p1，坐标为 (1, 2)
p1 = Point(1, 2)
# 创建一个 Point 类的实例 p2，坐标为 (4, 6)
p2 = Point(4, 6)
# 打印 p1 对象的字符串表示形式 
print(p1)
# 打印 p2 对象的字符串表示形
print(p2)
# 调用 p1 的 distance_to 方法，计算 p1 到 p2 的距离并打印结果
print(p1.distance_to(p2))
