from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference


wb = Workbook(write_only=True)
# 在工作簿中创建一个新的工作表
sheet = wb.create_sheet()

# 定义要写入Excel的数据，包含表头和销售数据
rows = [
    ('类别', '销售A组', '销售B组'),  # 表头行：类别名称和两个销售组
    ('手机', 40, 30),               # 手机类别的销售数据
    ('平板', 50, 60),               # 平板类别的销售数据
    ('笔记本', 80, 70),             # 笔记本类别的销售数据
    ('外围设备', 20, 10),           # 外围设备类别的销售数据
]

# 遍历数据行并将其添加到工作表中
for row in rows:
    sheet.append(row)

# 创建一个柱状图对象
chart = BarChart()
# 设置图表类型为垂直柱状图（'col'表示column，垂直柱形图；'bar'表示水平条形图）
chart.type = 'col'
# 设置图表样式为内置样式10（预设的视觉样式，包含颜色和布局）
chart.style = 10
# 设置图表的标题文本
chart.title = '销售统计图'
# 设置图表纵轴（Y轴）的标题文本
chart.y_axis.title = '销量'
# 设置图表横轴（X轴）的标题文本
chart.x_axis.title = '商品类别'
# 定义图表的数据来源范围
# Reference参数说明：工作表对象, 起始列=2, 起始行=1, 结束行=5, 结束列=3
# 即引用B1到C5的数据区域（销售A组和销售B组的所有数据）
data = Reference(sheet, min_col=2, min_row=1, max_row=5, max_col=3)
