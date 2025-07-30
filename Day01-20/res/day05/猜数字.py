import random
answer = random.randint(1,101)
counter = 0
while True:
  counter += 1
  num = int(input('请输入一个数字：'))
  if num > answer:
    print('猜大了')
  elif num < answer:
    print('猜小了')
  else:
    print('恭喜你猜对了')
    break
print(f'你一共猜了{counter}次')