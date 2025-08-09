# def add(*args):
#   total = 0
#   for _ in args:
#     if type(_) in (int, float):
#       total += _
#   return total


# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add(1,2,'hello',3,10))






def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)