# ^_^ coding: utf-8


# 统计特殊字符的次数函数statistic
def statistic_str(str_mes):
    result = {"letters": 0, "spaces": 0, "numbers": 0, "others": 0}
    for mes in str_mes:
        if mes.isdigit():
            result["numbers"] = result["numbers"] + 1
        elif mes.isspace():
            result["spaces"] = result["spaces"] + 1
        elif mes.isalpha():
            result["letters"] = result["letters"] + 1
        else:
            result["others"] = result["others"] + 1
    return result

if __name__ == "__main__":
    mes1 = input("输入要统计的字符串：")
    res1 = statistic_str(mes1)
    stat_str_model = "the statistic infos: letters:{r[letters]}, " \
                     "spaces:{r[spaces]}, numbers:{r[numbers]}, " \
                     "others:{r[others]}"
    print(stat_str_model.format(r=res1))

