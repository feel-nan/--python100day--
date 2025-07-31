# 找到100到999之间的水仙花数
for num in range(100,1000):
  low = num % 10
  mid = num // 10 % 10
  high = num // 100
  if num == low ** 3 + mid ** 3 + high ** 3:
    print(num)


# 对于一个 $n$ 位数（$n\geq3$），如果它每个位上的数字的 $n$ 次幂之和等于它本身，那么这个数就被称为水仙花数。