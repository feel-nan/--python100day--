# import random
# red_balls = list(range(1,34))
# selected_balls = []
# for _ in range(6):
#   index = random.randrange(len(red_balls))
#   selected_balls.append(red_balls.pop(index))
# selected_balls.sort()
# for ball in selected_balls:
#   print(f'\033[031m{ball:0>2d}\033[0m',end=' ')
# bule_ball = random.randrange(1,17)
# print(f'\033[034m{bule_ball:0>2d}\033[0m',end=' ')

import random
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
selected_ball = random.sample(red_balls,6)
selected_ball.sort()
for ball in selected_ball:
  print(f'\033[031m{ball:0>2d}\033[0m',end=' ')
bule_ball = random.sample(blue_balls,1)
print(f'\033[034m{bule_ball[0]:0>2d}\033[0m',end=' ')
