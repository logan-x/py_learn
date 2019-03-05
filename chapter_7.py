import time
import functools


# 装饰器
def decorate(func):
    return func


@decorate
def target():
    print('running target()')


# 上面代码效果和下面写法一样
# def target():
# print('running target()')
# target = decorate(target)

# 装饰器通常在一个模块中定义，再应用到其他模块中的函数上
# 大多数装饰器会在内部定义一个函数，然后将其返回

# 闭包
# 计算移动平均值
def make_averager():
    # 自由变量，临时变量需要nonlocal修饰
    series = []

    # averager 的闭包延伸到作用域之外，包含自由变量series
    def averager(new_value):
        series.append(new_value);
        total = sum(series);
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))


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


@clock
def factorial(n, **kwargs):
    return 1 if n < 2 else n * factorial(n - 1, **kwargs)


print(factorial(6, kw=6))
