# 素数指的是只能被 1 和自身整除的正整数（不包括 1）
for num in range(2,100):
  is_prime = True
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print(num, end='  ')