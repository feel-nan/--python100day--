# def fac(num):
#   if num in (0,1):
#     return 1
#   return num * fac(num - 1)

# print(fac(5))


# def fib1(n):
#   if n in(1,2):
#     return 1
#   return fib1(n - 1) + fib1(n - 2)


# for i in range(1,10):
#   print(fib1(i))


def fib2(n):
  a,b = 1,1
  for i in range(n):
    a,b = b,a+b
  return a

for i in range(1,10):
  print(fib2(i))
