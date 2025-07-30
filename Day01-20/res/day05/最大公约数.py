# x = int(input('请输入一个数字：'))
# y = int(input('请输入一个数字：'))
# for i in range(x,0,-1):
#   if x % i == 0 and y % i ==0:
#     print(f'最大公约数为{i}')
#     break

x = int(input())
y = int(input())
while y % x != 0:
  x,y = y,x % y
print(x)