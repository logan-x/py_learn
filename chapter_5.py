# 生成 html 标签
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def tag(name, *args, cls = None, **kw):
    """生成一个或多个html标签"""
    if cls is not None:
        kw['class'] = cls

    attr_str = ''

    if kw:
        attr_str = ''.join(f' {attr}="{value}"' for attr, value in sorted(kw.items()))

    if args:
        return '\n'.join(f'<{name}{attr_str}>{c}<{name}/>' for c in args)
    else:
        return f'<{name}{attr_str} />'

print(tag('br'))
print(tag('p', 'hello', 'world', id=33,cls='sider'))
print(tag(content='testing', name='img'))

# 可以使用**将字典所有元素作为单个参数传入
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))