score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade = }')



# 插一个三角形周长面积、
a = float(input('请输入三角形边长a:'))
b = float(input('请输入三角形边长b:'))
c = float(input('请输入三角形边长c:'))
if a+b > c and a+c > b and b+c > a:
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f'周长为:{a+b+c}')
    print(f'面积为:{area}')
else:
    print('输入的边长不能构成三角形')
