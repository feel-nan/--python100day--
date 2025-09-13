import xlwt
import random  # 补充缺失的random模块导入

# 学生姓名列表
student_names = ['张三', '李四', '王五', '赵六', '钱七']

# 生成5名学生的3门课程成绩（分数范围50-100）
scores = [[random.randrange(50,101) for _ in range(3)] for _ in range(5)]

# 创建Excel工作簿对象
wb = xlwt.Workbook()

# 添加名为'人工智能23-1'的工作表
sheet = wb.add_sheet('人工智能23-1')

# 表头标题列表
titles = ['姓名', 'Python', '机器学习', '深度学习']

# 写入表头（第0行）
for index, title in enumerate(titles):
    sheet.write(0, index, title)  # 行号0表示表头行


# 写入学生数据（从第1行开始）
for row in range(len(student_names)):
    # 写入学生姓名（第0列）
    sheet.write(row + 1, 0, student_names[row])
    
    # 写入对应课程成绩（从第1列开始）
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])


# header_style = xlwt.XFStyle()
# pattern = xlwt.Pattern()
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# # 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色
# pattern.pattern_fore_colour = 5
# header_style.pattern = pattern
# # titles = ('姓名', 'Python', '机器学习', '深度学习')
# # for index, title in enumerate(titles):
# #     sheet.write(0, index, title, header_style)

# # for row_idx, student_name in enumerate(student_names, start=1):  # 使用start=1确保从第1行开始
# #     sheet.write(row_idx, 0, student_name)
# #     for col_idx, score in enumerate(scores[row_idx - 1], start=1):  # col_idx从1开始
# #         sheet.write(row_idx, col_idx, score)

# font = xlwt.Font()
# font.name = '楷体'
# font.bold = True
# font.height = 20 * 18
# font.colour_index = 1
# font.italic = False
# header_style.font = font


# align = xlwt.Alignment()
# # 垂直方向的对齐方式
# align.vert = xlwt.Alignment.VERT_CENTER
# # 水平方向的对齐方式
# align.horz = xlwt.Alignment.HORZ_CENTER
# header_style.alignment = align


# borders = xlwt.Borders()
# props = (
#     ('top', 'top_colour'), ('right', 'right_colour'),
#     ('bottom', 'bottom_colour'), ('left', 'left_colour')
# )
# # 通过循环对四个方向的边框样式及颜色进行设定
# for position, color in props:
#     # 使用setattr内置函数动态给对象指定的属性赋值
#     setattr(borders, position, xlwt.Borders.DASHED)
#     setattr(borders, color, 5)
# header_style.borders = borders



wb.save(r'D:\学习python100day计划\Day21-30\res\Day24\人工智能23-1班成绩单.xls')