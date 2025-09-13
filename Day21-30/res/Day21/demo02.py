class InputError(ValueError):
    pass


def fac(num):
    if num < 0:
        raise InputError("输入错误，不能为负数")
    if num in (0,1):
        return 1
    return num * fac(num - 1)

flag = True
while flag:
    num = int(input('n='))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)