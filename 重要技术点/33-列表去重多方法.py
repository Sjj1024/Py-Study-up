 1 #利用集合，直接将列表转化为集合，自动去重后转回列表。有一个问题，转换为集合的同时，数据无序了。
 2 # li = [11,22,22,33,44,44]
 3 # set = set(li)
 4 # li = list(set)
 5 # print(li)
 6 #
 7 #
 8 # 第二种运用新建字典的方式，去除重复的键
 9 #  list = [11,22,33,22,44,33]
10 # dic = {}
11 # list = dic.fromkeys(list).keys()#字典在创建新的字典时，有重复key则覆盖
12 # print(list)
13 #
14 #
15 #
16 #第三种是用列表的推导
17 # list = [11,22,33,22,44,33]
18 # lis = []                          #创建一个新列表
19 # for i in list:                    #循环list里的每一个元素
20 #     if  i  not in lis:            #判断元素是否存在新列表中，不存在则添加，存在则跳过，以此去重
21 #         lis.append(i)
22 # print(lis)
23 #
24 #
25 #
26 #第四种仅仅只是将for循环变为while循环
27 # list = [11,22,33,22,44,33]
28 # result_list=[]
29 # temp_list=list
30 # i=0
31 # while i<len(temp_list):
32 #     if temp_list[i] not in result_list:
33 #         result_list.append(temp_list[i])
34 #     else:
35 #         i+=1
36 # print(result_list)
