# > **要求**：输入一个圆的半径（$\small{r}$），计算出它的周长（ $\small{2 \pi r}$ ）和面积（ $\small{\pi r^{2}}$ ）
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

import math
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)