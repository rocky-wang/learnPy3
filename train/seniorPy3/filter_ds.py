# coding: utf-8
# python高级编程技巧实战之数据结构相关话题
# 2-1 如何在列表,字典, 集合中根据条件筛选数据
"""
1、过滤列表中的负数 [3,9,-1,10,20,-2...]
2、筛选出字典中值高于90的项{'LiLei':79, 'Jim':88, 'Lucy':92, ...}
3、筛选出集合中能被3整除的元素{77, 89, 32, 20...}
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 通用做法：迭代 + 判断
# 高级做法：
# ---------------------------------------------------
# | 列表： 使用filter函数或列表解析
#           filter(lambda x: x>=0,data)
#           [x for x in data if x > 0]
# ---------------------------------------------------
# | 字典： 使用字典解析
#           {k:v for k, v in d.iteritems() if v > 90}
#       py3:{k:v for k, v in d.items() if v > 90}
# ---------------------------------------------------
# | 集合： 使用集合解析
#           {x for x in s if x % 3 == 0}
# ---------------------------------------------------
# * 不管是filter还是解析表达式，都是返回一个新的空间，而不会改变
# * 原有空间的值。
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from random import randint


# 过滤列表中的负数
def common_list(li):
    res = []
    for item in li:
        if item > 0:
            res.append(item)
    return res


# 筛选出字典中的值
def common_dict(arg_dict):
    res = {}
    for (k, v) in arg_dict.items():
        if v >= 90:
            res[k] = v
    return res


# 筛选出集合中的值
def common_set(arg_set):
    res = set()
    for item in arg_set:
        if item % 3 == 0:
            res.add(item)               # 注意add和update的区别，update传递的是一个迭代值
    return res


def test01():
    t1_lis = [1, 5, -9, -2, 0, 6, 10, -8]
    t1_dict = {'LiLei': 79, 'Jim': 88, 'Lucy': 92, 'Green': 90}
    t1_sets = {6, 89, 32, 33, 20}
    print(common_list(t1_lis))
    print(common_dict(t1_dict))
    print(common_set(t1_sets))

# py2使用xrange(10)，py3使用range(10)
t2_lis = [randint(-10, 10) for _ in range(10)]
t2_dict = {x: randint(60, 110) for x in range(1, 21)}
t2_set = set(t2_lis)

if __name__ == "__main1__":
    print("the list data is {}".format(t2_lis))
    # 使用filter/map函数进行过滤，py3返回的结果是一个iterators，所以需要进行一次展开，py2还是list
    tr2_lis = filter(lambda x: x >= 0, t2_lis)          # list(filter(lambda x: x >= 0, t2_lis))
    print("tr2 list is {}".format(list(tr2_lis)))

    # ----------------- 列表推导式方式 ----------------------
    tr3_list = [x for x in t2_lis if x >= 0]
    print("tr3 list is {}".format(tr3_list))
    # ----------------- 字典推到式方式 ----------------------
    print("the dict is {}".format(t2_dict))
    tr2_dict = {k: v for (k, v) in t2_dict.items() if v >= 90}
    print("the filter dict is {}".format(tr2_dict))
    # ---------------- 集合推到式方式 -----------------------
    print("the set is {}".format(t2_set))
    tr2_set = {x for x in t2_set if x % 3 == 0}
    print("the filter set is {}".format(tr2_set))

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("[x for x in t2_lis if x > 0]", setup="from __main__ import t2_lis"))
    print(timeit.timeit("common_list(t2_lis)", setup="from __main__ import t2_lis, common_list"))
    print("--------------------------------------------------------")
    print(timeit.timeit("common_dict(t2_dict)", setup="from __main__ import t2_dict, common_dict"))
    print(timeit.timeit("{k: v for (k, v) in t2_dict.items() if v >= 90}", setup="from __main__ import t2_dict"))
    print("--------------------------------------------------------")
    print(timeit.timeit("{x for x in t2_set if x % 3 == 0}", setup="from __main__ import t2_set"))
    print(timeit.timeit("common_set(t2_set)", setup="from __main__ import t2_set, common_set"))




