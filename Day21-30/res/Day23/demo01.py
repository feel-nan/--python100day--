import csv
import random


with open('data.csv', 'w')as file:
    writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['张三', '李四', '王五', '赵六', '钱七']
    for name in names:
        scores = [random.randrange(60, 100) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)

