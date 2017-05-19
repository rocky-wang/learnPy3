# ^_^ coding: utf-8


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


bakadd = add

print(bakadd(10, 20))
print(add(10, 100))

