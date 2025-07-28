# 判断闰年的规则是：
# 1. 公元年份非 4 的倍数是平年；
# 2. 公元年份为 4 的倍数但非 100 的倍数是闰年；
# 3. 公元年份为 400 的倍数是闰年

# 要求：输入一个 1582 年以后的年份，判断该年份是不是闰年。
year = int(input('请输入一个 1582 年以后的年份: '))
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap_year:
    print('%d年是闰年' % year)
else:
    print('%d年不是闰年' % year)
# print(f'{is_leap_year = }')