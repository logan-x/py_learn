import time
import functools
from functools import singledispatch
from collections import abc
import numbers
import html


# 输出函数运行时间的装饰器
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        # 记录初始时间
        t0 = time.perf_counter()

        # 调用源函数，保存返回结果
        result = func(*args, **kwargs)

        # 计算经过的时间
        elapsed = time.perf_counter() - t0

        # 格式化输出函数用时
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={w}' for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print(f'{elapsed:0.8f}s {name}({arg_str}) -> {result}')
        return result

    return clocked


# 使用缓存实现，速度更快
# maxsize: 指定存储多少个调用的结果，满了之后，旧的会被扔掉，为了性能，应设为2的幂
# typed: 为True则把不同参数类型分开保存，如浮点数和整数参数（1和1.0）区分开
@functools.lru_cache(maxsize=128, typed=False)
@clock
def fibonacci(n, **kwargs):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# 使用单分派函数，将整体方案拆分成多个模块
# 根据传入参数的类型做不同处理
# 注册的专门函数应该处理抽象基类
@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


# 注册str类型
@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<p>{content}</p>'


# 注册int类型，numbers.Integral 是int的虚拟超类
@htmlize.register(numbers.Integral)
def _(n):
    return f'<pre>{n} (0x{n:x})</pre>'


# 可叠放多个装饰器，支持不同类型
@htmlize.register(tuple)
@htmlize.register(abc.MutableMapping)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return f'<ul>\n<li>{inner}</li>\n</ul>'


print(fibonacci(30))
print(htmlize((1, '12', 2)))
