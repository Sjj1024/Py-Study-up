

def rep_mazi(ma, first, second):
    """
    替换邀请码中隐藏的内容，
    :param ma: 邀请码字符串
    :param first: 是第一次出现星号的位置替换为什么
    :param second: 第二次出现星号的位置替换成什么
    :return: 返回替换后的字符串
    """
    print("替换邀请码")
    ma_list = list(ma)
    first_index = ma_list.index("*")
    ma_list[first_index] = first
    second_index = ma_list.index("*")
    ma_list[second_index] = second
    res_ma = "".join(ma_list)
    return res_ma


def run():
    yaoqingma = "Additional*Spurio*"
    alpha = ["a", "b", "c", "d", "e", "f"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in numbers:
        for alp in alpha:
            first_ma = rep_mazi(yaoqingma, num, alp)
            second_ma = rep_mazi(yaoqingma, alp, num)
            print(first_ma, 111111111)
            print(second_ma, 222222222222222)


if __name__ == '__main__':
    run()
