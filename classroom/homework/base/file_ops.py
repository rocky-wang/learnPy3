# ^_^ coding: utf-8


def input_log_tofile(filename):
    while True:
        mes1 = input("请输入文件内容，exit或者quit退出： ")
        if mes1 in ("exit", "quit"):
            with open(filename, "r", encoding="utf-8") as fp1:
                for buf in fp1.readlines():
                    print(buf, end="")
            break
        else:
            with open(filename, "a", encoding="utf-8") as fp:
                fp.write(mes1 + "\n")
    return True

if __name__ == "__main__":
    input_log_tofile("input.log")
