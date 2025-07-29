# x = float(input('请输入一个数字:'))
# if x > 1:
#   y = 3*x-5
# elif x >= -1:
#   y = x + 2
# else:
#   y = 5*x + 3
# print('y =',y)


# 根据需要，中间还能嵌套if语句
x = float(input('请输入一个数字:'))
if x > 1:
  y = 3*x-5
else:
  if x >= -1:
    y = x+2
  else:
    y = 5*x+3
print('y =',y)
