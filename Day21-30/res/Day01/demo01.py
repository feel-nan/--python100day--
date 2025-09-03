# file = open(r"Day21-30\res\Day01\是你.txt", 'r', encoding='utf-8')
# for line in file:
#     print(line, end='')
# file.close()

# lines = file.readlines()
# for line in lines:
#     print(line, end='')
# file.close()
file = open(r"Day21-30\res\Day01\是你.txt", 'a', encoding='utf-8')
file.write('\n标题：《无题》')
file.write('\n作者：李商隐')
file.close()