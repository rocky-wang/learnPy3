# ^_^ coding: utf-8


# 装饰器(Decorator)，代码运行期间增加功能，但不改变原有功能的
def check(fn):
    def wrapper(a, b):
        print('check...')
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)
        print('variable cannot be add')
        return
    return wrapper


@check
def add(a1, a2):
    return a1 + a2


def mux(a1, a2):
    return a1 * a2

bakmux = mux
mux = check(mux)

print(bakmux(20, 5))
print(mux(20, 6))

bakadd = add

print(bakadd(10, 20))
print(add(10, 100))

