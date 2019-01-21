# 装饰器
def decorate(func):
    return func;

@decorate
def target():
    print('running target()')

# 上面代码效果和下面写法一样
# def target():
#     print('running target()')
# target = decorate(target)

# 装饰器通常在一个模块中定义，再应用到其他模块中的函数上
# 大多数装饰器会在内部定义一个函数，然后将其返回

# 使用装饰器的策略模式
