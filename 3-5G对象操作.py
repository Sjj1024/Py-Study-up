from openpyxl import load_workbook
from openpyxl import Workbook
import re

"""
将5G表格转换成需要的格式，然后存储成ecxel表格
"""


class GnrcChannel(object):
    wb1 = load_workbook('5GNRChannel办公.xlsx')
    wb2 = Workbook()

    def __init__(self):
        # 获取表格中所有表名字，是一个列表
        self.gnrc_sheets = self.wb1.sheetnames

    # 读取原始表格中的数据，并返回字典，
    def get_info_gnrc(self):
        # 通过表名字获取指定表
        sheet_name = "N1_15kHz"
        sheet = self.wb1[sheet_name]
        # 输出表的最大行和最大列
        print(sheet.max_row)
        print(sheet.max_column)
        # 读取表中的数据Bandwidth [MHz],Carrier centre,
        # 读出每一行所有值
        col_dict = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J',
                    '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R'}
        word_value_list = []  # 第一行对应每一列数据的列和值，元祖（列号和值）
        for i in sheet['1']:
            # print(i.row, i.column, i.value)
            word_value_list.append((col_dict[str(i.column)], i.value))
        print(word_value_list)
        # 获取指定列中有效数字的行和值列表，元祖（行号，值）
        num_value_list = []
        print(22222222222222)
        for col, val in word_value_list:
            if val in ['Bandwidth [MHz]']:
                for x in sheet[col]:
                    # 判断获取到的有效值是否是int，如果是None，将其赋值和上层行一样的值
                    # print(x.row, x.value)
                    if isinstance(x.value, int):
                        num_value_list.append((str(x.row), x.value))
                    elif x.value is None and num_value_list and isinstance(num_value_list[-1:][0][1], int):
                        num_value_list.append((str(x.row), num_value_list[-1:][0][1]))
        print(num_value_list)
        print(33333333333333)
        # 获取up系列的值，先判断是否有符号&，符号实在第三列C中,先获取到C列值，判断&是否在其中,在其中的就从之前的Down中获取up值
        c_value_list = []
        for i in sheet['C']:
            c_value_list.append(i.value)
        # 找到需要的数据，以列的形式保存到字典中，键是列中有效数字
        sheet_value_dict = dict()
        # 遍历行,获取到Down系列的值
        for row, val in num_value_list:  # 里面每个元素表示数字一行系列，元祖（row行号，值）
            # 遍历列
            data_value_list = []  # 保存一系列数据中列的值
            for col, word in word_value_list:  # 每个元素表示一列，元祖（col字母列号和值）
                # 符号不在其中的话，说明有up列的数据，所以需要再获取up的数据，
                if "&" not in c_value_list:
                    # print("&&&&&&&&&&不在其中")
                    # 遍历列号，获取到有效行中每一列的值，如果获取到的值为None，则取上一行的值
                    if sheet[col + str(int(row))].value is None:
                        sheet[col + str(int(row))].value = sheet[col + str(int(row)-1)].value
                    # 将获取到的行值保存到一个列表中，表示一行数据
                    data_value_list.append(sheet[col + str(int(row))].value)
                    # print(sheet[col + str(int(row))].value, end=",")  # 这里只表示一个单元格的值，遍历完才表示一行的数据
                else:
                    # 否则的话说明&在，就只需要从down中拼接up的数据
                    print("&&&&&&&&&&在其中")
                    # 遍历行实现加一行操作
                    print(sheet[col + row].value)
            sheet_value_dict[row] = data_value_list
        # print(sheet_value_dict)
        for key, value in sheet_value_dict.items():
            print(key, value)
    # 清洗原始表格中的数据，返回需要的样式数据
    def wash_info_gnrc(self):
        pass

    # 保存成新表格样式表
    def save_new_sheet(self):
        pass

    # 保存excel表格
    def save_excel(self):
        pass

    # 主程序
    def run(self):
        # 获取原始表格信息
        self.get_info_gnrc()
        # 清洗数据

        # 保存表信息到表中

        # 保存表格到指定文件

        pass


if __name__ == '__main__':
    gnrc = GnrcChannel()
    print("----------程序开始执行------------")
    gnrc.run()
    print("----------程序执行结束------------")
