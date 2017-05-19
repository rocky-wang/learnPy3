# ^_^ coding: utf-8

# 本例子主要展示python中的map/reduce高阶函数的使用事例
# 利用高阶函数reduce统计集合数据中出现的次数
# reduce函数迭代组合元素，每一次迭代，都将上一次的迭代结果（注：第一次为init元素，如果没有指定init则为seq的第一个元素）与下一个元素一同传入二元func函数中去执行
# 利用初始化一个空间来达到循环更新这个空间的情况
from functools import reduce


def statistics(dic, k):
    """
    利用reduce函数，第一个参数是迭代元素，第二个参数是下面一个值
    :param dic: 统计的结果的字典空间
    :param k: 判断在字典里是否包含这个key值
    :return: 更新后的字典
    """
    if k not in dic:
        dic[k] = 1
    else:
        dic[k] += 1
    return dic


def char2num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}[c]


def accumulate(x, y):
    if y == '.':
        return x
    return x*10 + y


def str2int(s):
    return reduce(accumulate, map(char2num, s))


def normalize(name):
    def convert(ele):
        tmp = ele.lower()
        return tmp.capitalize()
    return list(map(convert, name))


def prod(li):
    def tmp(x, y):
        return x * y
    return reduce(tmp, li)


def str2float(x):
    t = x.index('.')
    if t > 0:
        findex = len(x) - t - 1
    else:
        findex = 0
    return reduce(accumulate, map(char2num, x)) / 10 ** findex

# 统计重复元素的出现次数，反馈一个结果字典信息
testContianer = (1, 2, 2, 1, 3, 4, 2, 1, 1, 4)
result = reduce(statistics, testContianer, {})
print(result)

# 字符串转整型十进制数
t1 = int('32411', 26)
print(t1)
print(str2int('43278'))

# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# normalize函数
t2 = ['adam', 'LISA', 'barT']
d2 = normalize(t2)
print(d2)

# 累积功能[3, 5, 7, 9]
t3 = [3, 5, 7, 9]
d3 = prod(t3)
print(d3)

# 字符串转浮点数
t4 = "123.435"
d4 = float(t4)
dd4 = str2float(t4)
print(dd4)
