from collections import namedtuple

# 列表推导
# 只用来创建列表，不超过两行
symbols = 'abcdefg'
print([ord(symbol) for symbol in symbols])

print([ord(symbol) for symbol in symbols if 99 < ord(symbol)])

# 笛卡儿积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

print([(color, size) for color in colors
       for size in sizes])

# 生成器表达式
print(tuple(ord(symbol) for symbol in symbols))

for tshirt in (f'{color} {size}' for color in colors
               for size in sizes):
    print(tshirt)

# 元组
lax_coordinates = (33.945, -118.408056)
traveler_ids = [('USA', '645868114'), ('BRA', '12348114'), ('ESP', '98798114')]

for passport in sorted(traveler_ids):
    print(f'%s/%s' % passport)

# 可以使用占位符
for country, _ in traveler_ids:
    print(f'{country}')

# 拆包
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.06, 8014)
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
_, remainder = divmod(*t)
print(remainder)

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest, c = range(5)
print(a, b, rest, c)

# 嵌套元组拆包
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 86.933, (45.689722, -539.691667))
]

for name, cc, pop, (latitude, longitude) in metro_areas:
    if 0 >= longitude:
        print(name, latitude, longitude)

# 具名元组，类名+类字段名
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (81561.565, -46.48))
print(tokyo, tokyo.name)

# 切片
l = [10, 20, 30, 40, 50, 60]

# 保留左边，在下标2的位置分割
print(l[:2])
# 保留右边
print(l[2:])

s = 'bicycle'

# 以间隔取值，这边是3
print(s[::3])
# 反向取值
print(s[::-1])
print(s[::-2])

# 切片赋值
l = list(range(10))
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100 error 就算只有单独的值，也要转换成可迭代序列